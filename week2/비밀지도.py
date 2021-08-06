#비밀지도
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        line = str(bin(i|j)[2:])
        line = line.rjust(n, '0')
        line = line.replace('1', '#').replace('0', ' ')
        answer.append(line)
    print(answer)
    return answer


if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    solution(n, arr1, arr2)
