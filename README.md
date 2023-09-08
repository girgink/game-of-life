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
* Input file name, output file name, and number of generations are provided as arguments to the script.
* The script reads the size of the grid and the initial pattern from the input file.
* It applies the [rules](#rules) for the number of generations indicated as an argument.
* It writes the final pattern to the output file.

## Input and output file format
* The first line indicates the width and height of the grid as unsigned integer values separated by a space.
* The other lines indicate the initial locations of the living cells. Each line has two unsigned integer values separated by space indicating vertical and horizontal coordinates of the living cells, respectively.
    * The top left cell has the coordinates of (0, 0)
    * Valid vertical coordinate values range between 0 - (height-1), increasing from top to bottom.
    * Valid horizontal coordinate values range between 0 - (width-1), increasing from left to right.

## Example

```
python game.py input.txt output.txt 2
```

Input:
```
5 5
0 0
2 1
2 2
3 2
3 4
```
[input.txt](test/input_5x5.txt)

Output:
```
5 5
1 1
2 3
3 1
3 3
4 2
```
[output.txt](test/output_5x5_2.txt)