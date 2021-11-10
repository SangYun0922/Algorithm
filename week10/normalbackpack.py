
n, k = map(int, input().split())
weight = [0]
value = [0]

for i in range(n) :
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]
# 이때, dp 2차원 배열의 행의 인덱스는 아이템의 인덱스를 나타내고, 열의 인덱스는 용량을 나타낸다.
# print(dp)
for i in range(1, n + 1) : # i 는 행의 인덱스
    for j in range(1, k + 1) : # j는 열의 인덱스
        if j < weight[i] : # 만약 현재 k의 용량이 현재 아이템의 무게보다 작다면
            dp[i][j] = dp[i-1][j] #넣지 않고 넘어간다.
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight[i]] + value[i])


print(dp[n][k])
