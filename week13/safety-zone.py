#백준 2468 안전영역
#낮은 지역부터 물에 잠기기 때문에, 한번 물에 잠기면 계속 물에 잠김
#따라서 한번 물에 잠겼다면, 해당값을 -1로 바꿔주어서 진행
#모든 영역이 물에 잠길때 까지 탐색 (DFS or BFS 사용)

import sys
from collections import deque
input = sys.stdin.readline

def init_list(rain_quantity) : #현재 비의 양을 기준으로 리스트 초기화
    for i in range(N) :
        for j in range(N) :
            visited[i][j] = False #방문했던 기록을 False로 초기화
            if (zone[i][j] <= rain_quantity) :
                zone[i][j] = -1 #현재 비의 양을 기준으로 높이가 작은 영역을 -1로 교체

def dfs(x, y) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range (0, 4) : #해당 좌표로 부터 상하좌우 순으로 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and ny >= 0 and nx <= N-1 and ny <= N-1) : #각 좌표들에 대한 조건설정, 현재 NxN 배열에서 밖으로 나가는지, 그리고 각 좌표가 양수인지 판별
                if (zone[nx][ny] != -1 and (visited[nx][ny] == False)) : #nx, ny로 이동한 좌표에 대한 영역이 물에 안잠겨 있고, 방문한 적이 없는지 판별
                    visited[nx][ny] = True #방문한 적이 없으므로 해당 영역을 방문했음으로 표기
                    queue.append((nx, ny)) #해당 지점을 다시 큐에 삽입

N = int(input())
max_quantity = 0
zone = []
visited = [[False] * N for _ in range(N)] #방문했는지에 대한 체크리스트
alive_zones = [] #각 비의 양을 기준으로 생존한 영역을 담는 리스트
for _ in range(N) : #비의 최대양 및 이차원 리스트에 값 삽입
    row = list(map(int, input().split()))
    if (max_quantity < max(row)) :
        max_quantity = max(row)
    zone.append(row)

for i in range(max_quantity) :
    zone_cnt = 0 #현재 비의 양을 기준으로 생존한 영역의 개수
    init_list(i)
    for j in range(N) :
        for k in range(N) :
            if (zone[j][k] == -1 or visited[j][k] == True) : #모든 지점에 대해서 탐색을 실행하긴하지만, 잠겼거나, 방문한 적이 있다면, 갈 필요가 없음
                continue
            else :
                zone_cnt += 1
                dfs(j, k)
    alive_zones.append(zone_cnt)

#print(alive_zones) #debug
print(max(alive_zones))