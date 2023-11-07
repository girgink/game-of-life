# Optimization Results

- Run 1, Run 2, and average (Avg) results are in seconds.
- Memory column indicates the grid memory used by the code in Mb.
- Test hardware:
  * Model: HP ZBook 14u G6
  * Processor: Intel Core i7-8565U CPU @ 1.80GHz, 1992 Mhz, 4 Cores, 8 Logical Processors
  * BIOS: HP R70 ver. 01.25.00, 26/06/23


## Revisions

| File                | Description                                                    |
|:------------------- |:-------------------------------------------------------------- |
| game-r0.py          | Original version                                               |
| game-r1.py          | Use a two-row temporary array for applying the rules           |
| game-r2.py          | Use bytearray instead of list of integers                      |
| game-r2-bitarray.py | Use bitarray instead of bytearray                              |
| game-r3.py          | Get rid of boundary checks by using a slightly larger grid     |
| game-r4.py          | Create empty temporary row instead of reusing the existing one |
| game-r5.py          | Simplify cell update                                           |
| game-r6.py          | Use a single count expression                                  |
| game-r7.py          | Use y0 and y1 for y-1 and y+1                                  |
| game-r8.py          | Use x0 and x1 for x-1 and x+1                                  |
| game-r8-bitarray.py | Use bitarray instead of bytearray                              |


## 1,000 x 1,000 Grid

| File                | Software      | Run 1 | Run 2 | Avg  | % Fast | Memory |
|:------------------- |:------------- | -----:| -----:| ----:| ------:| ------:|
| game-r0.py          | Python 3.8.10 | 0.96  | 0.95  | 0.96 | 100.00 |  15.38 | 
| game-r1.py          | Python 3.8.10 | 0.95  | 0.94  | 0.95 | 101.06 |   7.69 |
| game-r2.py          | Python 3.8.10 | 1.00  | 1.00  | 1.00 |  95.50 |   1.02 |
| game-r2-bitarray.py | Python 3.8.10 | 1.00  | 1.02  | 1.01 |  94.55 |   0.20 |
| game-r3.py          | Python 3.8.10 | 0.78  | 0.80  | 0.79 | 120.89 |   1.02 |
| game-r4.py          | Python 3.8.10 | 0.75  | 0.73  | 0.74 | 129.05 |   1.02 |
| game-r5.py          | Python 3.8.10 | 0.72  | 0.72  | 0.72 | 132.64 |   1.02 |
| game-r6.py          | Python 3.8.10 | 0.66  | 0.67  | 0.67 | 143.61 |   1.02 |
| game-r7.py          | Python 3.8.10 | 0.50  | 0.48  | 0.49 | 194.90 |   1.02 |
| game-r8.py          | Python 3.8.10 | 0.37  | 0.37  | 0.37 | 258.11 |   1.02 |
| game-r8-bitarray.py | Python 3.8.10 | 0.37  | 0.37  | 0.37 | 258.11 |   0.20 |

**Summary**:
- Code optimization results in a speed up of about 2.5x.
- Use of bitarray with 2 temporary rows results in a memory reduction of about 120x.
- Use of bitarray instead of bytearray does not affect the performance.  


## 10,000 x 10,000 Grid

| File                | Software       | Run 1  | Run 2  | Avg    | % Fast   | Memory  |
|:------------------- |:-------------- | ------:| ------:| ------:| --------:| -------:|
| game-r0.py          | Python 3.8.10  | 106.10 | 106.90 | 106.50 |   100.00 | 1527.10 |
| game-r1.py          | Python 3.8.10  | 106.56 | 109.11 | 107.84 |    98.76 |  763.55 | 
| game-r2.py          | Python 3.8.10  | 107.67 | 108.74 | 108.21 |    98.42 |   95.99 |
| game-r2-bitarray.py | Python 3.8.10  | 108.25 | 111.16 | 109.71 |    97.08 |   12.77 |
| game-r3.py          | Python 3.8.10  |  87.76 |  84.12 |  85.94 |   123.92 |   95.99 |
| game-r4.py          | Python 3.8.10  |  84.06 |  83.19 |  83.63 |   127.35 |   95.99 |
| game-r5.py          | Python 3.8.10  |  78.88 |  80.28 |  79.58 |   133.83 |   95.99 |
| game-r6.py          | Python 3.8.10  |  74.77 |  73.97 |  74.37 |   143.20 |   95.99 |
| game-r7.py          | Python 3.8.10  |  49.05 |  51.28 |  50.17 |   212.30 |   95.99 |
| game-r8.py          | Python 3.8.10  |  37.63 |  38.66 |  38.15 |   279.20 |   95.99 |
| game-r8-bitarray.py | Python 3.8.10  |  38.17 |  38.93 |  38.55 |   276.26 |   12.77 |
| game-r0.py          | Python 3.12.0  |  81.49 |  81.61 |  81.55 |   130.59 | 1527.10 |
| game-r1.py          | Python 3.12.0  |  82.89 |  83.72 |  83.31 |   127.84 |  763.55 | 
| game-r2.py          | Python 3.12.0  |  92.61 |  91.91 |  92.26 |   115.43 |   95.99 |
| game-r2-bitarray.py | Python 3.12.0  |  96.57 |  96.03 |  96.30 |   110.59 |   12.77 |
| game-r3.py          | Python 3.12.0  |  75.09 |  75.22 |  75.16 |   141.71 |   95.99 |
| game-r4.py          | Python 3.12.0  |  69.79 |  70.65 |  70.22 |   151.67 |   95.99 |
| game-r5.py          | Python 3.12.0  |  63.76 |  64.18 |  63.97 |   166.48 |   95.99 |
| game-r6.py          | Python 3.12.0  |  59.47 |  58.66 |  59.07 |   180.31 |   95.99 |
| game-r7.py          | Python 3.12.0  |  40.90 |  40.87 |  40.89 |   260.49 |   95.99 |
| game-r8.py          | Python 3.12.0  |  32.93 |  32.40 |  32.67 |   326.04 |   95.99 |
| game-r8-bitarray.py | Python 3.12.0  |  36.11 |  37.24 |  36.68 |   290.39 |   12.77 |
| game-r0.py          | PyPy 7.3.13    |   2.62 |   2.59 |   2.61 |  4088.29 | 1527.10 |
| game-r1.py          | PyPy 7.3.13    |   2.72 |   2.72 |   2.72 |  3915.44 |  763.55 | 
| game-r2.py          | PyPy 7.3.13    |   2.64 |   2.63 |   2.64 |  4041.75 |   95.99 |
| game-r2-bitarray.py | PyPy 7.3.13    | 409.14 | 401.64 | 405.39 |    26.27 |   12.77 |
| game-r3.py          | PyPy 7.3.13    |   1.41 |   1.41 |   1.41 |  7553.19 |   95.99 |
| game-r4.py          | PyPy 7.3.13    |   1.34 |   1.37 |   1.36 |  7859.78 |   95.99 |
| game-r5.py          | PyPy 7.3.13    |   1.25 |   1.26 |   1.26 |  8486.06 |   95.99 |
| game-r6.py          | PyPy 7.3.13    |   1.25 |   1.24 |   1.25 |  8554.22 |   95.99 |
| game-r7.py          | PyPy 7.3.13    |   1.12 |   1.11 |   1.12 |  9551.57 |   95.99 |
| game-r8.py          | PyPy 7.3.13    |   1.05 |   1.04 |   1.05 | 10191.39 |   95.99 |
| game-r8-bitarray.py | PyPy 7.3.13    | 273.11 | 262.63 | 267.87 |    39.76 |   12.77 |
| game-r8.cpp         | gcc 10.3.0 -O3 |   0.35 |   0.34 |   0.35 | 30869.57 |   11.92 |

**Summary**:
- Use of Python 3.12 instead of 3.8 results in a speed up of about 0.17x for the optimized code (r8).
- Use of bitarray in Python 3.12 has a slight impact on the performance.
- Use of PyPy instead of Python results in a speed up of about 110x for the optimized code (r8).
- Use of bitarray in PyPy has a major impact on the performance resulting in about 255x slower run for the optimized code (r8).
- C++ implementation is about 3x faster than PyPy and has 8x less memory utilization.


## 100,000 x 100,000 Grid

| File        | Software       | Run 1  | Run 2  | Avg    | % Fast | Memory  |
|:----------- |:-------------- | ------:| ------:| ------:| ------:| -------:|
| game-r8.py  | PyPy 7.3.13    | 110.88 | 109.46 | 110.17 | 100.00 | 9543.32 |
| game-r8.cpp | gcc 10.3.0 -O3 |  36.55 |  35.46 |  36.01 | 305.99 | 1192.09 |

**Summary**:
- C++ implementation is about 3x faster than PyPy and has 8x less memory utilization.
