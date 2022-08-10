# 서로 다른 부분 문자열의 개수(11478)
# https://www.acmicpc.net/problem/11478
# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.
# ababc의 부분 문자열 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc (중복 X : 12)

import sys
S = sys.stdin.readline().strip()

results = dict()

for i in range(len(S)):
    for j in range(i, len(S)):
        word = S[i:j + 1]
        if word not in results:
            results[word] = 1

print(len(results))
