
def solution(nums):
    answer = 0
    choose = len(nums)/2 #짝수이므로 항상 나누어떨어짐
    kinds = set(nums) #nums에 set을 취해주어서, 해당 배열에 있는 폰켓몬의 종류가 몇가지인지 추출
    if len(kinds) >= choose : #만약 현재 배열의 가짓수가 내가 고를수 있는 개수보다 많다면,
        answer = choose #가능한 최대 가짓수는 내가 고를수 있는 만큼이 될것
    else : #반대일 경우
        answer = len(kinds)  #현재 종류의 가짓수 만큼 내가 최대로 고를수 있을것이다.
    #print(answer) debug
    return answer


if __name__ == '__main__':
    nums = input().split()
    nums = list(map(int, nums))
    solution(nums)
