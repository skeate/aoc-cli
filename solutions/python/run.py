import getopt
import importlib
import sys

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "y:d:")
    d = 1
    y = 2015
    for opt, arg in opts:
        if opt == '-d':
            d = int(arg)
        if opt == '-y':
            y = int(arg)
    sol = importlib.import_module(f'{y:04}.{d:02}')
    sol.run(sys.stdin.readlines())
