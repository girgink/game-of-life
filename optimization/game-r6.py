import sys
import time


def read_grid(inp):
    with open(inp) as f:
        w, h = map(int, f.readline().split())
        grid = []
        for y in range(h + 2):
            grid.append(bytearray(w + 2))
        for line in f:
            y, x = map(int, line.split())
            grid[y + 1][x + 1] = 1

    return grid


def save_grid(grid, filename):
    with open(filename, "w") as f:
        h, w = len(grid), len(grid[0])
        f.write(f"{w - 2} {h - 2}\n")
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    f.write(f"{y - 1} {x - 1}\n")


def tick(grid):
    h, w = len(grid), len(grid[0])
    temp = [None, None]
    for y in range(1, h - 1):
        temp[(y - 1) % 2] = row = bytearray(w)
        for x in range(1, w - 1):
            count = (
                grid[y - 1][x - 1]
                + grid[y - 1][x]
                + grid[y - 1][x + 1]
                + grid[y][x - 1]
                + grid[y][x + 1]
                + grid[y + 1][x - 1]
                + grid[y + 1][x]
                + grid[y + 1][x + 1]
            )
            if count == 3:
                row[x] = 1
            elif count == 2:
                row[x] = grid[y][x]

        if y > 1:
            grid[y - 1] = temp[y % 2]

    grid[h - 2] = temp[(h - 1) % 2]


def main():
    try:
        inp = sys.argv[1]
    except IndexError:
        sys.exit("No input filename.")

    try:
        out = sys.argv[2]
    except IndexError:
        sys.exit("No output filename.")

    try:
        print(f"Reading {inp}...")
        grid = read_grid(inp)
    except FileNotFoundError:
        sys.exit("Input file not found.")

    size = sys.getsizeof(grid)
    for row in grid:
        size += sys.getsizeof(row)
    print("Size of grid: {} MB".format(round(size / 2**20, 2)))

    try:
        n = int(sys.argv[3])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")

    start = time.time()

    for i in range(n):
        print(f"Tick {i}...")
        tick(grid)

    print("{} seconds elapsed for {} generations.".format(round(time.time() - start, 2), n))

    print(f"Writing {out}...")
    save_grid(grid, out)


if __name__ == "__main__":
    main()
