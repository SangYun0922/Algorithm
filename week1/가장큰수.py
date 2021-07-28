
def solution(numbers):
    answer = ''
    max_num = max(numbers)
    len_str = len(str(max_num))
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * len_str, reverse = True)
    for i in range(0, len(numbers)) :
        answer = answer + numbers[i]
    if answer < '1' :
        answer = '0'
    return answer


if __name__ == '__main__':
    numbers = input().split()
    numbers = list(map(int, numbers))
    solution(numbers)
