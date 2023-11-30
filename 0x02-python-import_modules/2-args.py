#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    name = sys.argv[0]
    args = sys.argv[1:]
    print("{} argument{}{}".format(len(args), "s" if len(
    args) != 1 else "", ":" if len(args) > 0 else "."))
    if len(args) > 0:
        index = 1
        for arg in args:
            print("{}: {} ".format(index, arg))
            index += 1
