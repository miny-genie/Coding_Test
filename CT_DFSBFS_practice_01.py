# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DFS(X, Y):
    if X < 0 or X >= row or Y < 0 or Y >= column:
        return False
    
    if mold[X][Y] == 0:
        mold[X][Y] = 1
        DFS(X-1, Y)
        DFS(X+1, Y)
        DFS(X, Y-1)
        DFS(X, Y+1)
        
        return True      
        
    return False

# ---------- Main ----------
row, column = map(int, input().split())
mold = []

for _ in range(row):
    mold.append(list(map(int, input().split())))
    
ice_cream = 0
for X in range(row):
    for Y in range(column):
        if DFS(X, Y):
            ice_cream += 1
            
print(ice_cream)