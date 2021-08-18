import sys

n = int(input())

lists = list(map(int, sys.stdin.readline().split()))  #맨 처음 첫 줄을 저장

for i in range(n - 1):
    temp = sorted(list(map(int, sys.stdin.readline().split())) + lists, reverse=True) #두 번째 줄부터 입력받아서 위의 맨 처음 첫줄과 합치고 해당 리스트를 내림 차순으로 정렬
    #print(temp)
    lists = temp[:n]  # 큰 순서대로 N개만 저장

print(lists[-1]) #해당 리스트중 맨끝 수를 가져옴