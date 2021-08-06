# 다시풀어야할듯..
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    total_weight = 0
    idx = 0
    N = len(truck_weights)

    now = 1
    q.append([now, truck_weights[idx]])
    total_weight += truck_weights[idx]
    idx += 1
    while True:
        now += 1
        if q:
            in_time, truck_weight = q.popleft()
            total_weight -= truck_weight
            if now - in_time < bridge_length:
                q.appendleft([in_time, truck_weight])
                total_weight += truck_weight
            if idx < N and total_weight + truck_weights[idx] <= weight:
                q.append([now, truck_weights[idx]])
                total_weight += truck_weights[idx]
                idx += 1
        else:
            break
    answer = now - 1
    print(answer) #debug
    return answer

if __name__ == '__main__':
    bridge_length = int(input())
    weight = int(input())
    truck_weights = list(map(int, input().split()))
    solution(bridge_length, weight, truck_weights)