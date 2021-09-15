n = int(input())
size = 101
res = 0
colorpaper = [[0] * size for i in range(size)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            colorpaper[j][k] = 2


for i in range(1, size):
    for j in range(1, size):
        if colorpaper[i][j] == 2:
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if (0 <= ni < size) and (0 <= nj < size):
                    if colorpaper[ni][nj] == 0:
                        res += 1
print(res)