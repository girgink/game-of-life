import sys
from game import create_input


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