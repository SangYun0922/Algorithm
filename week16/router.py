#백준 2110번 공유기 설치
import sys
input = sys.stdin.readline

N,C = list(map(int, input().split()))
array = sorted([int(input()) for _ in range(N)])

start = 1
end = max(array) - min(array)
ans = 0
while start <= end :
    mid = (start + end) // 2
    cnt = 1
    cur_h = array[0]
    for i in range(1, N):
        if array[i] - cur_h >= mid:
            cnt += 1
            cur_h = array[i]

    if cnt >= C:
        start = mid + 1
        ans = mid
    else :
        end = mid - 1

print(ans)
