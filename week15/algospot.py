#백준 1261번 알고스팟
#BFS, 단 모든 지역을 뒤질때, 방문했던 곳은 가지 말아야한다.
#0이 있던곳은 무조건 우선적으로 가자, 따라서, 우선적으로 가기 위해서 popleft를 사용하자
from collections import deque
import sys
input = sys.stdin.readline

def BFS() :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = int(0)
    queue = deque()
    visited[0][0] = 0
    queue.append((0,0))

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1) :
                if (maze[nx][ny] == 1) :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif (maze[nx][ny] == 0) :
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny)) #0이 있으면 무조건 먼저 가야하기 때문에

M, N = map(int, input().split())
maze = [list(map(int, input().replace("\n",""))) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
cnt = BFS()

print(visited[N-1][M-1])
