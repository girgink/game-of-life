import sys
import os.path
import random
import time


def grid_dims(grid):
    return len(grid), len(grid[0])


def read_grid(inp):
    with open(inp) as f:
        w, h = map(int, f.readline().split())
        grid = []
        for y in range(h):
            grid.append([0] * w)
        for line in f:
            y, x = map(int, line.split())
            grid[y][x] = 1

    return grid


def save_grid(grid, filename):
    with open(filename, "w") as f:
        w, h = grid_dims(grid)
        f.write(f"{w} {h}\n")
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    f.write(f"{y} {x}\n")


def save_grid_as_rle(grid, filename, overwrite=False):
    if os.path.exists(filename) and not overwrite:
        raise FileExistsError

    w, h = grid_dims(grid)

    with open(filename, "w") as f:
        f.write(f"x = {w}, y = {h}, rule = B3/S23:P{w},{h}\n")
        str = ""
        val = None
        run = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if val is None:
                    val = cell
                    run = 1
                elif val == cell:
                    run += 1
                else:
                    str += "{}{}".format(run if run > 1 else "", "o" if val == 1 else "b")
                    if len(str) > 68:
                        f.write(f"{str}\n")
                        str = ""
                    val = cell
                    run = 1
            if val is not None:
                str += "{}{}".format(run if run > 1 else "", "o" if val == 1 else "b")
                val = None
            str += "$"
            if len(str) > 68:
                f.write(f"{str}\n")
                str = ""

        f.write(f"{str}!\n")


def create_grid(w, h, alive=0.5, filename=None, overwrite=False):
    if alive < 0 or alive > 1.0:
        raise ValueError("Invalid alive percentage.")

    if not filename:
        filename = f"input_{w}x{h}_{alive}.txt"

    if os.path.exists(filename) and not overwrite:
        raise FileExistsError

    m = round(w * h * alive)
    skip = {}

    with open(filename, "w") as f:
        f.write(f"{w} {h}\n")
        while m > 0:
            x, y = random.randrange(w), random.randrange(h)
            idx = y * w + x
            if idx not in skip:
                f.write(f"{y} {x}\n")
                skip[idx] = True
                m -= 1

def tick(grid):
    w, h = grid_dims(grid)
    temp = []
    for y in range(h):
        temp.append([0] * w)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            count = 0
            if y > 0:
                count += grid[y - 1][x - 1] if x > 0 else 0
                count += grid[y - 1][x]
                count += grid[y - 1][x + 1] if x < w - 1 else 0
            count += grid[y][x - 1] if x > 0 else 0
            count += grid[y][x + 1] if x < w - 1 else 0
            if y < h - 1:
                count += grid[y + 1][x - 1] if x > 0 else 0
                count += grid[y + 1][x]
                count += grid[y + 1][x + 1] if x < w - 1 else 0

            if cell and count >= 2 and count <= 3:
                cell = 1
            elif not cell and count == 3:
                cell = 1
            else:
                cell = 0

            temp[y][x] = cell

    return temp


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
        grid = tick(grid)

    print("{} seconds elapsed for {} generations.".format(round(time.time() - start, 2), n))

    print(f"Writing {out}...")
    save_grid(grid, out)


if __name__ == "__main__":
    main()
