# 16928 번
import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())

    move = []

    for _ in range(M):
        x, y = map(int, input().split())
        move.append((x,y))

    for _ in range(N):
        u, v = map(int, input().split())
        move.append((u,v))

    move_start = [i[0] for i in move]
    move_end = [i[1] for i in move]

    visited = [-1 for _ in range(101)]

    def BFS(start):
        que = deque()
        que.append(start)
        visited[start] = 0

        while que:
            now = que.popleft()

            for dice in range(1,7):
                next = now + dice

                if next >= 1 and next <= 100:

                    if next in move_start:
                        index = move_start.index(next)
                        next = move_end[index]

                    if visited[next] == -1 or visited[next] > visited[now]+1:
                        que.append(next)
                        visited[next] = visited[now]+1


    BFS(1)
    print(visited[100])

solution()
