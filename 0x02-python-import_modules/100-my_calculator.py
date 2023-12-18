#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub,mul, div

    argLen = len(sys.argv) - 1
    print("length",argLen)

    if argLen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        for arg in sys.argv:
            if(arg[2] not in ['+', '-', '*', '/']):
                print (arg[2])

        



