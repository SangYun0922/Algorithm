n = int(input())
matrix = [[0 for i in range(101)] for i in range(101)] # 0~100까지의 2차원 좌표평면에 해당하는 2차원배열을 0으로 초기화 및 생성
res = 0

for i in range(n) :
    x, y = map(int, input().split()) # x, y는 각각 색종이의 좌측하단의 x, y좌표가 된다.
    for j in range(x, x + 10) : # 색종이의 한 변의 길이가 10이므로
        for k in range(y, y + 10) : # 색종이의 넓이만큼 2차원 배열에 1로 바꿔준다.
            matrix[j][k] = 1

for i in range(0, 101): # loop를 돌면서, 2차원 배열의 값이 1인 원소 하나하나마다 상하좌우를 체크하여 0과 맞닿아있는곳을 찾는다.
    for j in range(0, 101): # 정상적으로 찾았으면, res에 1만큼 더해주고, 값이 1인 모든원소에 대해서 수행해준다.
        if matrix[i][j] == 1:
            if matrix[i-1][j] == 0:
                res = res + 1
            if matrix[i+1][j] == 0:
                res = res + 1
            if matrix[i][j-1] == 0:
                res = res + 1
            if matrix[i][j+1] == 0:
                res = res + 1
print(res)
