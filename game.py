import sys
from array import *

def main():
    try:
        _, inp, out = sys.argv
    except ValueError as err:
        exit("Invalid number of arguments.")
        
    with open(inp) as f:
        w, h = map(int, f.readline().split())
        grid = []
        for y in range(h):
            grid.append([0] * w)
        n = int(f.readline())
        for line in f:
            x, y = map(int, line.split())
            grid[x][y] = 1

if __name__ == "__main__":
    main()
