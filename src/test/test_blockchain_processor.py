import unittest
from unittest.mock import Mock, patch
from tempfile import TemporaryDirectory
import configparser
import json
import shutil

from src.blockchain_processor import BlockchainProcessor

tmp_dir = TemporaryDirectory("electrum-test").name


class MockBitcoind:
    data_getblockhash = {
        0: '{"id": "jsonrpc", "error": null, "result": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"}'
    }

    data_getblock = {
        "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f":
            '{"result":{"hash":"000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f","confirmations":402077,"size":285,"height":0,"version":1,"merkleroot":"4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b","tx":["4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"],"time":1231006505,"mediantime":1231006505,"nonce":2083236893,"bits":"1d00ffff","difficulty":1,"chainwork":"0000000000000000000000000000000000000000000000000000000100010001","nextblockhash":"00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"},"error":null,"id":"jsonrpc"}',

    }

    def __init__(self, url, data=None):
        self.url = url
        if data:
            self.data = json.loads(data.decode("utf-8"))

    def read(self):
        if hasattr(self, "data_" + self.data["method"]):
            return getattr(self, "data_" + self.data["method"])[self.data["params"][0]]
        return json.dumps(getattr(self, "handle_" + self.data["method"])(*self.data["params"]))

    def close(self):
        pass

    def handle_getblockhash(self, block):
        if block == 0:
            return {"id": "jsonrpc", "error": None,
                    "result": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"}


class BlockchainProcessorTest(unittest.TestCase):
    config = configparser.ConfigParser()
    config["leveldb"] = {
        "path": tmp_dir,
        "hist_cache": 6710886,
        "utxo_cache": 13421772,
        "addr_cache": 1677721,
        "pruning_limit": 1000,
        "profiler": False
    }
    config["bitcoind"] = {
        "bitcoind_user": "bit",
        "bitcoind_password": "jkadfgldfhgdfgdfg",
        "bitcoind_host": "arcadia.bauerj.eu",
        "bitcoind_port": "8332"
    }

    # Mock threading, we don't want the BlockchainProcessor to fork
    @patch('src.blockchain_processor.threading')
    # Mock urlopen so we can intercept requests to bitcoind
    @patch('src.blockchain_processor.urllib.request.urlopen', side_effect=MockBitcoind)
    def setUp(self, mock_threading, mock_urlopen):
        self.shared = Mock()
        self.shared.stopped.return_value = False
        self.processor = BlockchainProcessor(BlockchainProcessorTest.config, self.shared)

    def tearDown(self):
        shutil.rmtree(tmp_dir)

    def test_here(self):
        pass


if __name__ == '__main__':
    unittest.main()
