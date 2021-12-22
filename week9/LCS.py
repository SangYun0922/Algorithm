def lengthLCS(S_m, T_n, S, T, L) :
    for i in range(S_m + 1) :
        L[i][0] = 0
    for i in range(T_n + 1) :
        L[0][i] = 0

    for i in range(1,S_m + 1) :
        for j in range(1,T_n + 1) :
            if (S[i-1] == T[j-1]) :
                L[i][j] = L[i-1][j-1] + 1
            else :
                L[i][j] = max(L[i][j-1], L[i-1][j])

S = list(input().upper())
T = list(input().upper())

S_m = len(S)
T_n = len(T)
L = [[0]*(T_n + 1) for i in range(S_m + 1)]
lengthLCS(S_m, T_n, S, T, L)

print(L[-1][-1])
