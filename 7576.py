# 7576 번
import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

def solution():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    graph = []
    M, N = map(int, input().split())

    for _ in range(N):
        sub_graph = list(map(int, input().split()))
        graph.append(sub_graph)

    # print(graph)

    def BFS(starts):
        que = deque()
        for start_x, start_y in starts:
            que.append((start_x, start_y))

        days = 0

        while que:
            now_x, now_y = que.popleft()
            for i in range(4):
                next_x = now_x + dx[i]
                next_y = now_y + dy[i]

                if next_x >= 0 and next_x < N and next_y >= 0 and next_y < M and graph[next_x][next_y] == 0:
                    graph[next_x][next_y] = graph[now_x][now_y] + 1
                    days = graph[now_x][now_y]
                    que.append((next_x, next_y))

        return days


    def search():
        starts = []
        result = -1
        for y in range(M):
            for x in range(N):
                # print(x,y, graph[x][y])
                if graph[x][y] == 1:
                    starts.append((x,y))

        if len(starts) != 0:
            result = BFS(starts)

            for y in range(M):
                for x in range(N):
                    # print(x,y, graph[x][y])
                    if graph[x][y] == 0:
                        return -1

        return result

    print(search())

solution()
