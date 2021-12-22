#백준 16929번 two dots
#d1,d2 ... dk로 사이클을 만들었을떄의 조건
#사이클을 만들기 위해서 필요한 점의 개수는 4개이상
#사이클의 속하는 점은 모두 서로다른 점들이다 다만, 색은 모두 같다.
#현재 좌표를 기준으로 이전에 방문한 지점의 좌표로는 가면 안됨
#즉, 이전 좌표로 가지 않았는데, 방문한 지점을 만났다면, 사이클 형성
import sys

def dfs(x, y ,tmp_x, tmp_y, dot) : #tmp_x, tmp_y는 기존 좌표, 즉 함수를 호출할 시점에서 인자로 준 좌표를 보존하기 위하여 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if (visited[x][y] == True) : #basecase, 만약 탐색하고자 하는 좌표가 이미 방문했다면, 사이클을 이룬것이므로, True 리턴
        return True

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx != tmp_x or ny != tmp_y : #이동하는 좌표가 이전좌표가 다를때
            if (nx >= 0 and ny >= 0 and nx < N and ny < M): #이동할 좌표가 범위안에 속하는지 확인하고
                if (dots[nx][ny] == dot): #이동하는 좌표의 색이 동일한 것만 탐색
                    if (dfs(nx, ny, x, y, dot)) : #이동한 좌표를 기준으로 재귀 호출로 재 탐색,
                        return True

    return False

def solution(N, M) :
    for i in range(N):
        for j in range(M):
            if (visited[i][j]) : #모든 지점에대해서 검사를 진행하나, 방문한적이 있다면 skip
                continue
            dot = dots[i][j]
            if dfs(i, j, i, j, dot) :
                print("Yes")
                return

    print("No")
    return

input = sys.stdin.readline
N, M = map(int, input().split())
dots = [list(input().replace("\n","")) for _ in range(N)] #개행문자를 제거하여 입력받자
visited = [[False] * M for _ in range(N)] #방문했는지에 대한 체크리스트
solution(N, M)
