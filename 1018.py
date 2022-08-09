#체스판 다시 칠하기
#8x8 이상 체스판 NxM 크기의 보드를 잘라서 체스판을 만든다
#왼쪽 상단을 시작(시작은 흑 or 백)
#경우의 수 (N-7)*(M-7)*2
#다시 칠해야 하는 정사각형의 최소 갯수 구하기

N, M = map(int, input().split())

board = [[None for col in range(M)] for row in range(N)]

for i in range(N):
    x = input()
    for idx in range(M):
        board[i][idx] = x[idx]

results = []

for i in range(N - 7):
    for j in range(M - 7):
        w_start = 0
        b_start = 0
        for x in range(8):
            for y in range(8):
                ans = None
                if (x + y) % 2 == 0:
                    ans = 'W'
                else:
                    ans = 'B'

                if board[i + x][j + y] != ans:
                    w_start = w_start + 1
                else:
                    b_start = b_start + 1

        results.append(min(w_start, b_start))

print(min(results))
