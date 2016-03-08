#!/usr/bin/env python
from timeit import timeit
from sys import version

if __name__ == '__main__':
    parse_test_setup="from src.deserialize import BCDataStream, parse_Transaction\nexample_tx_bytes = b'\\x01\\x00\\x00\\x00\\x01{\\x1e\\xab\\xe0 \\x9b\\x1f\\xe7\\x94\\x12Eu\\xef\\x80pW\\xc7z\\xda!8\\xaeO\\xa8\\xd6\\xc4\\xde\\x03\\x98\\xa1O?\\x00\\x00\\x00\\x00\\x00\\xff\\xff\\xff\\xff\\x01\\xf0\\xca\\x05*\\x01\\x00\\x00\\x00\\x19v\\xa9\\x14\\xcb\\xc2\\nvd\\xf2\\xf6\\x9eSU\\xaaBpE\\xbc\\x15\\xe7\\xc6\\xc7r\\x88\\xac\\x00\\x00\\x00\\x00'"
    parse_test_run="vds = BCDataStream()\nvds.write(example_tx_bytes)\nparsed_tx = parse_Transaction(vds, is_coinbase=False)"
    print("Running...")
    time = timeit(parse_test_run, parse_test_setup, number=100000)
    print("Took {} seconds in {}".format(time, version))