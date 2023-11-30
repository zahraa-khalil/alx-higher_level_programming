#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    name = sys.argv[0]
    argv = sys.argv[1:]
    print("{} argument{}{}".format(len(argv), "s" if len(
    argv) != 1 else "", ":" if len(argv) > 0 else "."))
    if len(argv) > 0:
        index = 1
        for arg in argv:
            print("{}: {} ".format(index, arg))
            index += 1
