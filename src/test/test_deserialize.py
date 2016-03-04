import unittest
try:
    from electrumserver.deserialize import BCDataStream, parse_Transaction
except ImportError:
    from src.deserialize import BCDataStream, parse_Transaction

class DeserializeTest(unittest.TestCase):
    example_tx_bytes = b'\x01\x00\x00\x00\x01{\x1e\xab\xe0 \x9b\x1f\xe7\x94\x12Eu\xef\x80pW\xc7z\xda!8\xaeO\xa8\xd6' \
        b'\xc4\xde\x03\x98\xa1O?\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\xf0\xca\x05*\x01\x00\x00\x00\x19v\xa9\x14' \
        b'\xcb\xc2\nvd\xf2\xf6\x9eSU\xaaBpE\xbc\x15\xe7\xc6\xc7r\x88\xac\x00\x00\x00\x00'

    def test_transaction_parsing(self):
        vds = BCDataStream()
        vds.write(self.example_tx_bytes)
        parsed_tx = parse_Transaction(vds, is_coinbase=False)
        expected_tx = {
            'inputs': [
                {
                    'prevout_n': 0,
                    'sequence': 4294967295,
                    'prevout_hash': b'3f4fa19803dec4d6a84fae3821da7ac7577080ef75451294e71f9b20e0ab1e7b'
                }
            ],
            'outputs': [
                {'value': 4999990000,
                 'raw_output_script': b'76a914cbc20a7664f2f69e5355aa427045bc15e7c6c77288ac',
                 'address': b'1KaNd8ybzTDYKpyMB9X2dstvMwo5ogo5bT',
                 'index': 0
                 }
            ],
            'version': 1,
            'lockTime': 0
        }
        self.assertEqual(parsed_tx, expected_tx)


if __name__ == '__main__':
    unittest.main()
