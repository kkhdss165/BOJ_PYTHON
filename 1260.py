# 1260 번
import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

def solution():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)

    visited_DFS = []
    visited_BFS = []

    values = []
    def DFS(start):
        # 출력
        print(start, end= ' ')
        visited_DFS.append(start)

        graph[start].sort()
        for next in graph[start]:
            if next not in visited_DFS:
                values.append(next)
                DFS(next)
                values.pop()

    def BFS(start):
        # 출력
        print(start, end= ' ')
        visited_BFS.append(start)

        que = deque()
        que.append(start)
        while que:
            now = que.popleft()
            graph[now].sort()
            for next in graph[now]:
                if next not in visited_BFS:
                    print(next, end=' ')
                    que.append(next)
                    visited_BFS.append(next)

    DFS(V)
    print()
    BFS(V)


solution()
