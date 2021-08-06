from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque(priorities)

    while dq:
        temp = dq.popleft()
        flag = True

        for priority in dq:
            if temp< priority:
                flag = False
                break
        if flag:
            answer += 1
            if location: location -= 1
            else:#print(answer) debug
                return answer
        else:
            dq.append(temp)
            location = (location - 1) if location else (len(dq) - 1)


if __name__ == '__main__':
    priorities = list(map(int, input().split()))
    location = int(input())
    solution(priorities, location)