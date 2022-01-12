#백준 3896번 소수 사이 수열
import sys
import math
input = sys.stdin.readline

def isPrime(k) :
    for i in range(2, int(k//2) + 1) :
        if k % i == 0 :
            return False
    return  True

def eratos(k) :
    max_num = 1299709
    s = [True] * max_num
    for i in range(2, int(math.sqrt(max_num)) + 1) :
        if s[i] == True:
            for j in range(i+i, max_num, i) :
                s[j] = False
    prime_list = [i for i in range(2, max_num) if s[i] == True]

    num_1 = max([i for i in range(2, k) if s[i] == True])
    num_2 = 0

    for i in range(2, len(prime_list)) :
        if (k < prime_list[i]) :
            num_2 = prime_list[i]
            break
    return num_2 - num_1

T = int(input())
for _ in range(T) :
    k = int(input())
    flag = isPrime(k)
    if (flag) :
        print(0)
        continue
    else :
        ans = eratos(k)
        print(ans)
