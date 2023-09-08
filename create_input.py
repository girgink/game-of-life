import sys
from game import create_grid


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
        opts["filename"] = sys.argv[5]

    if num_args > 5:
        val = str(sys.argv[6]).upper()
        opts["overwrite"] = val in ["YES", "Y", "1", "TRUE"]

    create_grid(w, h, **opts)


if __name__ == "__main__":
    main()