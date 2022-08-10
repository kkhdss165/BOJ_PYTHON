# 숫자카드(10815)
# https://www.acmicpc.net/problem/10815
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서,
# 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
# 시간초과로 가지고 있는 숫자카드 중복을 제거(성공)

import sys

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for number in numbers:
    if number in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
