import sys


def grid_dims(grid):
    return len(grid), len(grid[0])


def read_input(inp):
    with open(inp) as f:
        w, h = map(int, f.readline().split())
        grid = []
        for y in range(h):
            grid.append([0] * w)
        for line in f:
            y, x = map(int, line.split())
            grid[y][x] = 1

    return grid


def write_output(grid, out):
    with open(out, "w") as f:
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
        grid = read_input(inp)
    except FileNotFoundError:
        sys.exit("Input file not found.")

    try:
        n = int(sys.argv[3])
    except IndexError:
        n = 10
    except ValueError:
        sys.exit("Invalid number of generations.")

    for i in range(n):
        grid = tick(grid)

    write_output(grid, out)


if __name__ == "__main__":
    main()