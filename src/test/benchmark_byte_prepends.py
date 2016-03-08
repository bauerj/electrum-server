if __name__ == '__main__':
    from timeit import timeit
    from sys import version

    basic_setup = "example_sequence = b'\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\t\\n\\x0b\\x0c\\r\\x0e\\x0f\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17\\x18\\x19\\x1a\\x1b\\x1c\\x1d\\x1e\\x1f !\"#$%&\\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\\x7f\\x80\\x81\\x82\\x83\\x84\\x85\\x86\\x87\\x88\\x89\\x8a\\x8b\\x8c\\x8d\\x8e\\x8f\\x90\\x91\\x92\\x93\\x94\\x95\\x96\\x97\\x98\\x99\\x9a\\x9b\\x9c\\x9d\\x9e\\x9f\\xa0\\xa1\\xa2\\xa3\\xa4\\xa5\\xa6\\xa7\\xa8\\xa9\\xaa\\xab\\xac\\xad\\xae\\xaf\\xb0\\xb1\\xb2\\xb3\\xb4\\xb5\\xb6\\xb7\\xb8\\xb9\\xba\\xbb\\xbc\\xbd\\xbe\\xbf\\xc0\\xc1\\xc2\\xc3\\xc4\\xc5\\xc6\\xc7\\xc8\\xc9\\xca\\xcb\\xcc\\xcd\\xce\\xcf\\xd0\\xd1\\xd2\\xd3\\xd4\\xd5\\xd6\\xd7\\xd8\\xd9\\xda\\xdb\\xdc\\xdd\\xde\\xdf\\xe0\\xe1\\xe2\\xe3\\xe4\\xe5\\xe6\\xe7\\xe8\\xe9\\xea\\xeb\\xec\\xed\\xee\\xef\\xf0\\xf1\\xf2\\xf3\\xf4\\xf5\\xf6\\xf7\\xf8\\xf9\\xfa\\xfb\\xfc\\xfd\\xfe\\xff'"

    print("On {},".format(version))
    test_bytearray_append_then_reverse = """thing=bytearray()
for byte in example_sequence:
    thing.append(byte)
result = thing[::-1]"""
    time = timeit(test_bytearray_append_then_reverse, basic_setup, number=10000)
    print('appending to a bytearray then reversing it takes {:.20f}s.'.format(time))


    setup_deque_appendleft = "from collections import deque\n" + basic_setup
    test_deque_appendleft = """thing=deque()
for byte in example_sequence:
    thing.appendleft(byte)
result = bytes(thing)"""
    time = timeit(test_deque_appendleft, setup_deque_appendleft, number=10000)
    print('Left-appending to a deque then converting to bytes takes {:.20f}s.'.format(time))

    test_concat_new_bytes = """thing=bytes()
for byte in example_sequence:
    thing = bytes((byte,)) + thing
result = thing"""
    time = timeit(test_concat_new_bytes, basic_setup, number=10000)
    print('Converting the int to a single-byte bytes then concatenating takes {:.20f}s.'.format(time))

    test_concat_sliced_bytes = """thing=bytes()
for i in range(0, len(example_sequence)):
    thing = example_sequence[i:i+1] + thing
result = thing"""
    time = timeit(test_concat_sliced_bytes, basic_setup, number=10000)
    print('Slicing single-byte bytes then concatenating takes {:.20f}s.'.format(time))