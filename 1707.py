# 1707 번
# 처음에는 테스트 케이스 갯수, 두번째부터 정점의 갯수 간선수
# 그룹 A를 1, 그룹 B를 -1로 설정한 뒤 BFS

import sys
from collections import deque
input = sys.stdin.readline

def solution():
    K = int(input().rstrip())

    for _ in range(K):

        V, E = map(int, input().split())

        graph = [[] for _ in range(V+1)]

        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        visited = [0 for _ in range(V+1)]

        def BFS(start):

            que = deque()
            que.append(start)
            visited[start] = 1

            while que:
                now = que.popleft()
                graph[now].sort()

                for next in graph[now]:
                    if visited[next] == 0:
                        visited[next] = visited[now] * -1
                        que.append(next)

                    elif visited[next] == visited[now]:
                        return False


            return True

        def search():
            for start in range(1,V+1):

                if visited[start] == 0:
                    result = BFS(start)

                    if result == False:
                        return 'NO'

            return 'YES'

        print(search())


solution()
