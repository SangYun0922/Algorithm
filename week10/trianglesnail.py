import numpy as np

def solution(n):
    answer = [[0] * n for i in range(n)]
    answer = edge(n, answer)
    answer = np.array(answer).flatten()
    answer = np.delete(answer, np.where(answer == 0)).tolist()

    return answer

def edge(n, matrix) :
    tmp = 1
    row = -1
    col = 0
    for i in range(n, 0 , -3) :
        for j in range(0, i):  # 왼쪽 변
            row += 1
            matrix[row][col] += tmp
            tmp += 1
        for j in range(0, i - 1):  # 밑 변
            col += 1
            matrix[row][col] += tmp
            tmp += 1
        for j in range(0, i - 2):  # 대각선 변
            row -= 1
            col -= 1
            matrix[row][col] = tmp
            tmp += 1
    return matrix
n = int(input())
solution(n)