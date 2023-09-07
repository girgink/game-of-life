import sys

def read_input(inp):
    with open(inp) as f:
        w, h = map(int, f.readline().split())
        grid = []
        for y in range(h):
            grid.append([0] * w)
        n = int(f.readline())
        for line in f:
            x, y = map(int, line.split())
            grid[y][x] = 1
    
    return w, h, grid
    
def write_output(w, h, grid, out):
    with open(out, "w") as f:
        f.write(f"{w} {h}\n")
        for y, line in enumerate(grid):
            for x, cell in enumerate(line):
                if cell:
                    f.write(f"{x} {y}\n")

def main():
    try:
        _, inp, out = sys.argv
    except ValueError as err:
        exit("Invalid number of arguments.")

    w, h, grid = read_input(inp)

    write_output(w, h, grid, out)

if __name__ == "__main__":
    main()
