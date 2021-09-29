N = int(input())

buildings = list(map(int, input().split()))
obs = [0] * N
result = int(0)

for i in range(N) :
    check = -1e9
    for j in range(i+1, N):
        gradient = (buildings[j] - buildings[i]) / (j - i)
        if gradient > check : #기울기가 이전 기울기 값보다 큰경우 업데이트
            check = gradient
            obs[i] += 1
            obs[j] += 1 #이때, i, j번째 건물에서 동시에 볼수 있다.

for _ in obs :
    result = max(result, _)
print(result)