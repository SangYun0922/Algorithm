#백준 7569번 토마토
#BFS

import sys
from collections import deque
input = sys.stdin.readline

def BFS() :
    dx = [-1, 1, 0, 0, 0, 0] #x축 방향 설정
    dy = [0, 0, -1, 1, 0, 0] #y축 방향 설정
    dz = [0, 0, 0, 0, -1, 1] #z축 방향 설정

    while queue :
        z, y, x = queue.popleft()
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if (0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomatos[nz][ny][nx] == 0) :
                tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
                queue.append((nz, ny, nx))

def check(cnt) :
    for i in tomatos:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    return
            cnt = max(cnt, max(j))
    print(cnt - 1)
    return

M, N, H = map(int, input().split())
cnt = int(0)
tomatos = []
queue = deque()
for z in range(H) :
    tmp = []
    for y in range(N) :
        tmp.append(list(map(int, input().split())))
        for x in range(M) :
            if (tmp[y][x] == 1) :
                queue.append((z, y, x)) #좌표는 (H, N, M)로 설정 즉, 기존 공간좌표인 (x, y, z)의 역순
    tomatos.append(tmp)

BFS()
check(cnt)
