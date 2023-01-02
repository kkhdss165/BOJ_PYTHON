# 7562 번
import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

def solution():
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]

    T = int(input())

    for _ in range(T):
        I = int(input())
        src_x, src_y = map(int, input().split())
        dst_x, dst_y = map(int, input().split())

        visited = [[-1 for _ in range(I)] for _ in range(I)]

        def BFS(start, end):
            start_x, start_y = start
            end_x, end_y = end

            que = deque()
            que.append((start_x, start_y))
            visited[start_x][start_y] = 0

            while que:
                now_x, now_y = que.popleft()

                if now_x == end_x and now_y == end_y:
                    print(visited[now_x][now_y])
                    return

                for i in range(8):
                    next_x = now_x + dx[i]
                    next_y = now_y + dy[i]

                    if next_x >= 0 and next_x < I and next_y >= 0 and next_y < I and visited[next_x][next_y] == -1:
                        visited[next_x][next_y] = visited[now_x][now_y] + 1
                        que.append((next_x, next_y))

        BFS((src_x, src_y), (dst_x, dst_y))

solution()
