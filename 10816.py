# 숫자 카드 2(10816)
# https://www.acmicpc.net/problem/10816
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서,
# 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
# 카운터 사전에 없으면 0 출력

import sys
from collections import Counter

N = int(sys.stdin.readline())
values = Counter(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
reqs = list(map(int, sys.stdin.readline().split()))
for req in reqs:
    print(values[req], end = " ")
