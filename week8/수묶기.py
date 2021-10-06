# 모든 수는 단 한번만 묶거나, 묶지 않아야 한다.
# 서로 다른 두 수를 묶기 위해서 필요한 규칙
# 양수의 경우 : 가장 큰 수와 두번째로 큰 수를 곱한것이 더한 것 보다 커야한다.
# 음수의 경우 : 음수는 음수끼리 묶어서 곱해주어 양수로 만든다.
# 0이 있을 경우 : 음수랑 곱해준다.
n = int(input())
numarr = [int(input()) for i in range(n)]

list_plus = []
list_minus = []

result = 0
for i in range(n) :
    elements = numarr.pop()
    if elements > 0 :
        list_plus.append(elements)
    else : # 0과 음수는 모아서 리스트에 넣는다.
        list_minus.append(elements)

list_plus = sorted(list_plus) # 오름차순 정렬로 가장 큰 값이 위로 오게 한다.
list_minus = sorted(list_minus, reverse=True) # 내림차순 정렬로 가장 작은 값이 위로오게 한다.


while len(list_plus) > 1 :
    plus_1 = list_plus.pop()
    plus_2 = list_plus.pop()  # 가장 큰 수와 그 다음수 2개를 pop
    if (plus_1 * plus_2) > (plus_1 + plus_2):
        result += (plus_1 * plus_2)
    else:
        result += (plus_1 + plus_2)

while len(list_minus) > 1 :
    minus_1 = list_minus.pop()
    minus_2 = list_minus.pop()
    result += minus_1 * minus_2


if list_plus :
    result += list_plus.pop()
if list_minus :
    result += list_minus.pop()
print(result)


