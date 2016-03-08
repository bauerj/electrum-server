from binascii import hexlify, unhexlify
import unittest
try:
    from electrumserver.utils import hash_160_to_address, bc_address_to_hash_160, header_from_string, header_to_string
except ImportError:
    from src.utils import hash_160_to_address, bc_address_to_hash_160, header_from_string, header_to_string


class UtilTest(unittest.TestCase):
    def test_hash_160_to_address(self):
        self.assertEqual(hash_160_to_address(None), None)
        self.assertEqual(hash_160_to_address(unhexlify('04e9fca1')), None)
        self.assertEqual(hash_160_to_address(unhexlify('04e9fca1f96e021dfaf35bbea267ec2c60787c1b1337')), None)
        self.assertEqual(hash_160_to_address(unhexlify('1ad3b0b711f211655a01142fbb8fecabe8e30b93')),
                         b'13SrAVFPVW1txSj34B8Bd6hnDbyPsVGa92')

    def test_bc_address_to_hash_160(self):
        self.assertEqual(bc_address_to_hash_160(None), None)
        self.assertEqual(bc_address_to_hash_160(b''), None)
        self.assertEqual(bc_address_to_hash_160(b'13SrAVFPVW1txSj34B8Bd6hnDbyPsVGa921337'), None)
        self.assertEqual(hexlify(bc_address_to_hash_160(b'13SrAVFPVW1txSj34B8Bd6hnDbyPsVGa92')),
                         b'1ad3b0b711f211655a01142fbb8fecabe8e30b93')

    def test_headers_from_string(self):
        block_hex = b"03000000855d154359b794c6ba2c5586cf6278eee5bd658faa954200000000000000000035e95b187fb0d5175f681c2" \
                    b"a1c499c3c91a0781c91679545a1fcabba2cd7cd801b04bd5515081518aa8afeaf020100000001000000000000000000" \
                    b"0000000000000000000000000000000000000000000000ffffffff25035b9d05384d2f040f04bd550894251c009a050" \
                    b"0000f5b4254434368696e612e636f6d5d20000000000100f90295000000001976a9142c30a6aaac6d96687291475d7d" \
                    b"52f4b469f665a688ac0000000001000000018651ed89909def949ee3e05631bb332f339f4c667b0af7e2d94e7940a45" \
                    b"68a21000000006a473044022059c947c745d94d1019990f39b2c938c9ce3e79fe9a650cff01589ec3b5ed2c2c02206d" \
                    b"cff5e15ae6aa9c7d44308f16963dd5ad1dd3229e923c9de3ae1c14f6f91a02012102163e80de410646145142636833d" \
                    b"8a92de4bb5c99e49bd52be5346fb1030628d4ffffffff0250ac6002000000001976a9145ca26d65ee83f441ef98b624" \
                    b"763a305d50eb36cf88aca0860100000000001976a914838eb1034b719f9c47ab853aee63d505e4176a8388ac00000000"
        block_bytes = unhexlify(block_hex)
        block_header_bytes = block_bytes[0:80]
        header = header_from_string(block_header_bytes)
        self.assertEqual(header['version'], 3)
        self.assertEqual(header['prev_block_hash'], b'0000000000000000004295aa8f65bde5ee7862cf86552cbac694b75943155d85')
        self.assertEqual(header['merkle_root'], b'80cdd72cbaabfca1459567911c78a0913c9c491c2a1c685f17d5b07f185be935')
        self.assertEqual(header['timestamp'], 1438450715)
        self.assertEqual(header['bits'], 404031509)
        self.assertEqual(header['nonce'], 2952694442)

    def test_headers_to_string(self):
        header = {
            'version': 1,
            'prev_block_hash': b'00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81',
            'merkle_root': b'2b12fcf1b09288fcaff797d71e950e71ae42b91e8bdb2304758dfcffc2b620e3',
            'timestamp': 1305998791,
            'bits': 440711666,
            'nonce': 2504433986,
        }
        header_hex = header_to_string(header)
        expected_header_hex = b'0100000081cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000e320b6c2fffc8' \
                              b'd750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122bc7f5d74df2b9441a42a14695'
        self.assertEqual(header_hex, expected_header_hex)


if __name__ == '__main__':
    unittest.main()
