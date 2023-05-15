# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(X, Y):
    queue = deque()
    queue.append((X, Y))
    
    # 큐가 빌 때까지 반복
    while queue:
        X, Y = queue.popleft()
        
        # 현재 위치 기준으로 네 방향 확인
        for direction in range(4):
            nx = X + dx[direction]
            ny = Y + dy[direction]
            
            # 미로 바깥으로 나간 경우
            if nx < 0 or nx >= row or ny < 0 or ny >= column:
                continue
            
            # 가려는 곳이 벽이거나 장애물인 경우
            if maze[nx][ny] == 0:
                continue
            
            # 갈 수 있는 경우
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[X][Y] + 1   # 나아가면서 동시에 cnt++
                queue.append((nx, ny))
    
    return maze[row-1][column-1]

# ---------- Main ----------
row, column = map(int, input().split())
maze = []

# UP, DN, RGT, LFT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]    
    
for _ in range(row):
    maze.append(list(map(int, input().rstrip())))
    
print(BFS(0 , 0))