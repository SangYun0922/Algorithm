
# 1334번 계속 틀리는중....^오^
s = str(input())
length = len(s)
half_even = s[:length//2]
half_odd = s[:(length + 1)//2] # 홀수 일 경우 half는 가운데값 까지 가져온다

#print(half_odd) debug
#print(half_odd[-1]) debug
def getPalindrome(num, len, half_even, half_odd) :
    if len == 1 : # 한자리 수일 때는 무조건 '11'이 그 다음으로 크다
        print(11)
    elif num == '9'* len : #만약 모든 자리수가 9일 경우에는 해당 값에 2만 더해주면 대칭이된다.
        print(int(num) + 2)
    elif len % 2 == 0 :     #길이가 짝수일때
        palindrome = half_even[:] + half_even[::-1]
        if int(num) < int(palindrome) :
            print(palindrome)
        else :
            half_even = str(int(half_even) + 1) #반 자른거에 1을 더한다
            palindrome = half_even[:] + half_even[::-1]
            print(palindrome)
    elif len % 2 == 1 : #길이가 홀수일때
        palindrome = half_odd[:] + half_odd[-2::-1] # 앞은 가운데 값을 포함하고, 뒤에는 가운데 값을 뺀 값만 뒤집어서 붙여준다.
        if int(num) < int(palindrome) :
            print(palindrome)
        else :
            half_odd = str(int(half_odd) + 1) # 가운데를 포함한 반 자른거에 1을 더한다. 최종적으로는 가운데 값에 1이 더해짐
            palindrome = half_odd[:] + half_odd[-2::-1]
            print(palindrome)


getPalindrome(s, length, half_even, half_odd)