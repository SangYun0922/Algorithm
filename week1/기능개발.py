
def solution(progresses, speeds):
    answer = []
    remain = []
    buffer = None
    for i in range(0, len(progresses)):
        tmp = 100 - progresses[i]
        remain.append(tmp)
    for i in range(0, len(speeds)):
        if remain[i] % speeds[i] == 0 :
            remain[i] = remain[i] // speeds[i]
        else :
            remain[i] = (remain[i] // speeds[i]) + 1
    for i in range(0, len(remain)) :
        if buffer == None :
            buffer = remain[i]
            answer.append(1)
        elif remain[i] <= buffer:
            answer[-1] +=1
        elif remain[i] > buffer :
            answer.append(1)
            buffer = remain[i]
    #print(answer) debug
    return answer


if __name__ == '__main__':
    progresses = input().split()
    progresses = list(map(int, progresses))
    speeds = input().split()
    speeds = list(map(int, speeds))
    solution(progresses, speeds)
