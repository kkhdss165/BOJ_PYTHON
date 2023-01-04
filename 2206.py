# 2206 번
# 벽 부시고 가기
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    M, N = map(int, input().split())

    matrix = []

    for _ in range(M):
        sub_matrix = list(map(int, input().rstrip()))
        matrix.append(sub_matrix)

    visited = [[[0 for _ in range(N)] for _ in range(M)]]+[[[0 for _ in range(N)] for _ in range(M)]]

    # print(matrix)
    # print(visited)

    def BFS(x, y, w):
        que = deque()
        que.append((x,y,w))
        visited[w][x][y] = 1
        # print(visited)

        while que:
            now_x, now_y, break_chance = que.popleft()
            # print(visited)

            if now_x == M-1 and now_y == N-1:
                return visited[break_chance][now_x][now_y]

            for i in range(4):
                next_x = now_x + dx[i]
                next_y = now_y + dy[i]

                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue

                #다음이 벽이고 찬스를 사용하지 않는 경우
                # print(next_x, next_y, break_chance)
                if matrix[next_x][next_y] == 1 and break_chance == 0:
                    visited[1][next_x][next_y] = visited[0][now_x][now_y] + 1
                    que.append((next_x, next_y, 1))

                #다음이 벽이 아닌 경우
                elif matrix[next_x][next_y] == 0 and visited[break_chance][next_x][next_y] == 0:
                    visited[break_chance][next_x][next_y] = visited[break_chance][now_x][now_y] + 1
                    que.append((next_x, next_y, break_chance))

        return -1

    print(BFS(0,0,0))
    # print(visited)

solution()
