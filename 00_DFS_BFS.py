# -------------------------------------------------- DFS, BFS --------------------------------------------------
# ---------- Import ----------
from collections import deque
import sys, time
input = sys.stdin.readline

# ---------- Function ----------
def DFS(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=" ")
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)
            
            
def BFS(graph, start, visited):
    # 큐(Queue) 구현을 위해 Deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        
        # 해당 원소와 연결된, 미방문한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True