string = str(input())
stk = []
tag = False
res = ""
for i in range(0, len(string)):
    if string[i] == '<':    # '<'로 태그가 시작될때,
        tag = True          # 먼저 tag 플래그를 true로 바꿔주고
        while stk:          # stk에 남아있는 스트링들을 pop시켜서 결과값에 더해준다.
            res = res + stk.pop()
    if tag == True:         # 만약 태그 플래그가 true인 상태에서는
        res = res + string[i] # 역순으로 바꿔줄 필요가 없으므로 그대로 결과값에 더해준다.
    if string[i] == '>':    # '>'가 나왔을경우에는, 태그가 끝나는 것이므 태그 플래그를 False로 바꿔준다.
        tag = False
        continue
    if tag == False and string[i] == ' ':   # tag가 아니고 string에 공백이 있을경우
        while (stk):                        # 공백이 나오기 전까지 담았던 것들을 모두 pop
            res = res + stk.pop()
        res = res + ' '                     # 결과값에 공백을 추가
    elif tag == False :                     # 태그도 공백도 아닐시 스택에 추가
        stk.append(string[i])

while (stk):                                # 태그, 공백도 없는 경우 stk에 남아있게 되는데, 남아있는걸 전부 결과값에 더해줌
    res = res + stk.pop()

print(res)