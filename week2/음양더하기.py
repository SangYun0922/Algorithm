

def solution(absolutes,signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == 'True':
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


if __name__ == '__main__':
    absolutes = list(map(int, input().split()))
    signs = list(map(int, input().split()))
    solution(absolutes,signs)
