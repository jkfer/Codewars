"""
3kyu:
------

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]

---
Idea:
1. find the possiblility count for the whole array (each point) - this means 9 - (number of distinct values of row + column + box)
2. fill the boxes that has the possibilities of 1. update possibilities (anything in the same row and column gets -1)
3. fill the boxes that has the possibilities of 1. update possi..........
.
.
.
4. do until all the possibilities are 0
"""


# get all cordinates within the 3 x 3 square of a given r, c value of a 9/9 value
def get_box(r, c, puzzle):
    # generate all the 3*3 points of the puzzle
    values = []

    def get_ran(v):
        if v <= 2:
            R = [0, 1, 2]
        elif 2 < v <= 5:
            R = [3, 4, 5]
        else:
            R = [6, 7, 8]
        return R
    
    for R in get_ran(r):
        for C in get_ran(c):
            if puzzle[R][C] != 0:
                values.append(puzzle[R][C])

    return values


def get_row(r, puzzle):
    return puzzle[r]

def get_col(c, puzzle):
    return [puzzle[i][c] for i in range(9)]

# traverse the puzzle and fill the possib dict for each position
def create_possibl(puzzle):
    # create array for the possibilities of numbers:
    points = [[i, j] for i in range(9) for j in range(9)]
    
    D = {}
    
    for point in points:
        r, c = point
        # Row:
        if puzzle[r][c] != 0:
            D[(r, c)] = 0
        else:
            # Row, Col and Box
            R = puzzle[r]
            C = [puzzle[i][c] for i in range(9)]
            B = get_box(r, c, puzzle)
            
            all = R + C + B
            # remove the 0s in here
            while 0 in all:
                all.remove(0)
            
            D[(r, c)] = 9 - len(set(all))
    return D


def fill_puzz(puzzle, D):
    for a, b in D.items():
        if b == 1:
            r, c = a
            S = get_row(r, puzzle) + get_col(c, puzzle) + get_box(r, c, puzzle)
            actual = range(1, 10)
            rem = list(set(actual).difference(S))[0]
            # update the puzzle
            puzzle[r][c] = rem
    
    D = create_possibl(puzzle)
    if 1 in D.values():
        return fill_puzz(puzzle, D)

    return puzzle


if __name__ == "__main__":
    # Ex:
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    D = create_possibl(puzzle)
    ans = fill_puzz(puzzle, D)
    print(ans)