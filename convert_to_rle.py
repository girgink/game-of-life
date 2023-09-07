import sys
import os.path
from game import read_input, grid_dims

def val_bool(val):
    val = str(val).upper()
    return val == "YES" or val == "Y" or val == "1" or val == "TRUE"
    
def convert_to_rle(inp, out = None, skip_n = False, overwrite = False):
    if not out:
        out = os.path.splitext(inp)[0] + ".rle"
    
    if os.path.exists(out) and not overwrite:
        raise FileExistsError

    grid, _ = read_input(inp, skip_n=skip_n)
    
    w, h = grid_dims(grid)
    
    with open(out, "w") as f:
        f.write(f"x = {w}, y = {h}, rule = B3/S23:P{w},{h}\n")
        str = ""
        val = None
        run = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if val == None:
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
    
def main():
    num_args = len(sys.argv)
    
    try:
        inp = sys.argv[1]
    except IndexError:
        exit("Invalid number of arguments.")
    
    opts = {}
    
    if num_args > 2:
        opts["out"] = str(sys.argv[2])

    if num_args > 3:
        opts["skip_n"] = val_bool(sys.argv[3])

    if num_args > 4:
        opts["overwrite"] = val_bool(sys.argv[4])
        
    convert_to_rle(inp, **opts)
    
if __name__ == "__main__":
    main()