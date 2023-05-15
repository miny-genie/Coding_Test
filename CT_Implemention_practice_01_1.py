# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
size = int(input())
directions = list(map(str, input().split()))

X, Y = 1, 1
move_types = ["U", "D", "L", "R"]
dx = [-1, 1, 0 ,0]
dy = [0, 0 ,-1, 1]

for direction in directions:
    for index in range(4):
        if direction == move_types[index]:
            nx = X + dx[index]
            ny = Y + dy[index]
            
    if nx > 5 or nx < 1 or ny > 5 or ny < 1:
        continue
    
    X, Y = nx, ny
    
print(X, Y)
        