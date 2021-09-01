n, m = map(int, input().split())

a = [list(map(int, list(input()))) for i in range(n)] #2차원 배열 만들기
b = [list(map(int, list(input()))) for i in range(n)]

count = int(0)
flag = int(1)
def change(row, column) :
    for i in range(row, row + 3) :
        for j in range(column, column + 3) :
            a[i][j] = 1 - a[i][j]

for i in range(0, n-2) :        # 3x3 부분행렬이 갈수 있는 최대범위
    for j in range(0, m-2) :
        if a[i][j] != b[i][j] : # a, b행렬을 다 비교해가면서 서로 다른 부분을 발견한다면,
            change(i ,j)        # 해당부분 값 바꾸기
            count = count + 1   # 값을 바꾸었으므로 count 1증가

for i in range(0, n) :          # 값을 다 바꾸어주었다면 루프를 돌면서 두 행렬이 같은지 판별
    for j in range(0, m) :
        if a[i][j] != b[i][j] :
            flag = 0
            break

if flag == 0 :
    print(-1)
else :
    print(count)