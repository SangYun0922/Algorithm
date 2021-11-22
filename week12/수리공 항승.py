N,L = map(int, input().split())
leak = sorted(list(map(int, input().split())))
result = 1
start = leak[0] - 0.5
end = start + L
for i in range(0,N) :
    if leak[i] > end :
        result += 1
        start = leak[i] - 0.5
        end = start + L

print(result)