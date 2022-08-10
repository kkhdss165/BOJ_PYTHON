# 문자열 집합(14425)
# https://www.acmicpc.net/problem/14425
# 정수 N과 M이 주어진다
# N개의 단어와 M개의 단어가 주어진다
# M개의 단어가 N개의 단어에 포함되어 있는 갯수를 구하시오


import sys

N, M = map(int, sys.stdin.readline().split())

n_words = []
m_words = []

for i in range(N):
    n_words.append(sys.stdin.readline().strip())

n_words = list(set(n_words))

for i in range(M):
    m_words.append(sys.stdin.readline().strip())

count = 0
for word in m_words:
    if word in n_words:
        count = count + 1

print(count)
