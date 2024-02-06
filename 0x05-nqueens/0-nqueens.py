#!/usr/bin/python3
import sys

def print_solution(solution):
    for pos in solution:
        print(pos)

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve_nqueens_util(board, row + 1, n, solutions)

def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
