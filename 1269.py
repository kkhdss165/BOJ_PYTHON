# 대칭 차집합(1269)
# https://www.acmicpc.net/problem/1269
# A = { 1, 2, 4 } 이고 B = { 2, 3, 4, 5, 6 } 라고 할 때
# A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

_, _ = map(int, input().split())
X = list(set(list(map(int, input().split()))))
A = dict()
for i, a in enumerate(X):
    A[a] = i

B = dict()
#중복 목록 C
C = dict()
X = list(set(list(map(int, input().split()))))
for i, b in enumerate(X):
    B[b] = i
    if b in A:
        C[b] = i

print(len(A)+len(B)-2*len(C))
