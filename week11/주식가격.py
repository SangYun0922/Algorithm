def solution(prices):
    length = len(prices)
    answer = [0]*length
    for i in range(0, length) :
        for j in range(i+1, length) :
            if prices[i] <= prices[j] : # 가격이 떨어지지 않는 경우, 해당 인덱스에 값을 계속 더해준다.
                answer[i] += 1
            else : # 만약 가격이 떨어졌다면, 1초뒤에 가격이 떨어진것이라 여기므로, 1초동안은 가격이 유지되므로 1을 더해주나, 그 즉시 루프에서 탈출
                answer[i] += 1
                break
    return answer

prices = list(map(int, input().split()))
answer = solution(prices)
print(answer)