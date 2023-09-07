# Conway's Game of Life
This is an implementation of Conway's Game of Life in Python.

## <a name="rules"></a>Rules
From [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):

* The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells
* Each cell is in one of two possible states, live or dead.
* Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
* At each step in time, the following transitions occur:
    1. Any **live** cell with *fewer than two live neighbours* **dies**, as if by underpopulation.
    2. Any **live** cell with *two or three live neighbours* **lives** on to the next generation.
    3. Any **live** cell with *more than three live neighbours* **dies**, as if by overpopulation.
    4. Any **dead** cell with *exactly three live neighbours* becomes a **live** cell, as if by reproduction.
* These rules can be condensed into the following:
    1. Any **live** cell with *two or three live neighbours* **survives**.
    2. Any **dead** cell with *three live neighbours* becomes a **live** cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Implementation
* The script reads the size of the grid, the number of generations to be simulated, and the initial pattern from a text file.
* It applies the [rules](#rules) for the number of generations indicated in the input fule.
* It writes the final pattern to a text file.

### <a href="input-file-format"></a>Input file format
* The first line indicates the width and height of the grid as unsigned integer values separated by a space.
* The second line indicates the number of generations to be simulated as unsigned integer.
* The other lines indicate the locations of the living cells initially. Each line has two unsigned integer values separated by space indicating zero-indexed horizontal and vertical coordinates of the living cells, respectively.
    * Valid horizontal coordinate values range between 0 - (width-1)
    * Valid vertical coordinate values range between 0 - (height-1)

Example:
```
5 5
2
0 0
2 1
2 2
3 2
3 4
```
[input.txt](test/input_5x5_2.txt)

### Output file format
* The first line indicates the width and height of the grid as unsigned integer values separated by a space.
* The other lines indicate the locations of the living cells initially. Each line has two unsigned integer values separated by space indicating zero-indexed horizontal and vertical coordinates of the living cells, respectively. See [input file format](#input-file-format) for details.

Example:
```
5 5
1 1
2 3
3 1
3 3
4 2
```
[output.txt](test/output_5x5_2.txt)
