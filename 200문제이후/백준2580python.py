import sys
sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
def search(y, x):
    nums = [i for i in range(1, 10)]
    for i in range(9):
        if sudoku[y][i] in nums:
            nums.remove(sudoku[y][i])
        if sudoku[i][x] in nums:
            nums.remove(sudoku[i][x])
    y //= 3
    x //= 3
    for i in range(y * 3, (y + 1) * 3):
        for j in range(x * 3, (x + 1) * 3):
            if sudoku[i][j] in nums:
                nums.remove(sudoku[i][j])
    return nums
def dfs(count):
    if count == len(zeros):
        for arr in sudoku:
            print(*arr)
        exit()
    (i, j) = zeros[count]
    array = search(i, j)
    for num in array:
        sudoku[i][j] = num
        dfs(count + 1)
        sudoku[i][j] = 0
dfs(0)
