#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1


# if __name__ == '__main__':
#     import sys
#     argv = sys.argv[1:]
#     print("{} argument{}{}".format(len(argv), "s" if len(
#         argv) != 1 else "", ":" if len(argv) > 0 else "."))
#     if len(argv) > 0:
#         index = 1
#         for arg in argv:
#             print("{}: {} ".format(index, arg))
#             index += 1


# lambda function 

# lambda x: 2 * x 
# lambda x,y: x + y
# mx = lambda x, y : x if x > y else y