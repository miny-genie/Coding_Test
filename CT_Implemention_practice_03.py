# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def lotation_left(direction):
    # 0 북, 1 동, 2 남, 3 서
    direction -= 1
    
    if direction < 0:
        direction = 3
    
    return direction

# ---------- Main ----------
row, column = map(int, input().split())
X, Y, direction = map(int, input().split())

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1] # 북, 동, 남, 서
path = [ [ 0 for _ in range(column) ] for _ in range(row) ]
path[X][Y] = 1     # 현재 위치 가봤다고 표시

lst = []
for _ in range(row):
    lst.append(list(map(int, input().split())))
    
# Start Traveling
cnt, turn_times = 1, 0
while True:
    direction = lotation_left(direction)
    nx = X + dx[direction]
    ny = Y + dy[direction]
    
    # 회전 후 안 가본 곳이 있다면
    if lst[nx][ny] == 0 and path[nx][ny] == 0:
        X, Y = nx, ny
        cnt += 1
        turn_times = 0
        path[nx][ny] = 1
        
    # 회전 후 가보지 않은 칸이 없거나 전부 바다인 경우
    else:
        turn_times += 1
           
    # 4군데 모두 갈 곳이 없는 경우
    if turn_times == 4:
        nx = X - dx[direction]
        ny = Y - dy[direction]
        
        # 뒤가 바다가 아니라면
        if lst[nx][ny] == 0:
            X, Y = nx, ny
            turn_times = 0
            
        # 뒤도 바다라면
        else:
            break
        
print(cnt)     
    