import sys
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
