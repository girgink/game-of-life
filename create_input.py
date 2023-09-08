import sys
import os.path
import random


def create_input(w, h, alive=0.5, n=10, filename=None, overwrite=False):
    if alive < 0 or alive > 1.0:
        raise ValueError("Invalid alive percentage.")

    if n < 1:
        raise ValueError("Invalid number of generations.")

    if not filename:
        filename = f"input_{w}x{h}_{alive}_{n}.txt"

    if os.path.exists(filename) and not overwrite:
        raise FileExistsError

    m = round(w * h * alive)
    skip = {}

    with open(filename, "w") as f:
        f.write(f"{w} {h}\n")
        f.write(f"{n}\n")
        while m > 0:
            x, y = random.randrange(w), random.randrange(h)
            idx = y * w + x
            if idx not in skip:
                f.write(f"{y} {x}\n")
                skip[idx] = True
                m -= 1


def main():

    num_args = len(sys.argv)

    try:
        w, h = int(sys.argv[1]), int(sys.argv[2])
    except IndexError:
        exit("Invalid number of arguments.")

    if w <= 0:
        raise ValueError("Invalid grid width.")

    if h <= 0:
        raise ValueError("Invalid grid height.")

    opts = {}

    if num_args > 3:
        opts["alive"] = float(sys.argv[3])

    if num_args > 4:
        opts["n"] = int(sys.argv[4])

    if num_args > 5:
        opts["filename"] = sys.argv[5]

    if num_args > 6:
        val = str(sys.argv[6]).upper()
        opts["overwrite"] = val in ["YES", "Y", "1", "TRUE"]

    create_input(w, h, **opts)


if __name__ == "__main__":
    main()