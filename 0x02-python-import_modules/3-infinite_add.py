#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(sys.argv)

    result = 0
    for i in range(1, argc):
        result += int(argv[i])

    print(result)
