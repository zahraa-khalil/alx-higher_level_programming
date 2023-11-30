#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    name = sys.argv[0]
    argv = sys.argv[1:]
    result = 0
    if len(argv) > 1:
        for arg in argv:
            result += int(arg)

        print("{}".format(result))

    else:
        print("{}".format(result))
