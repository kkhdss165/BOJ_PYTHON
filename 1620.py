# 나는야 포켓몬 마스터 이다솜(1620)
# https://www.acmicpc.net/problem/1620
# 정수 N과 M이 주어진다
# N개의 포켓몬의 이름이 들어오고
# M개의 포켓몬 이름 또는 숫자가 들어온다
# 숫자인 경우 인덱스로 이름을 출력하고, 이름의 경우 인덱스를 출력한다

import sys

N, M = map(int, sys.stdin.readline().split())

poke_dict = {}

for i in range(1, N+1):
    pokemon = sys.stdin.readline().strip()
    poke_dict[i] = pokemon
    poke_dict[pokemon] = i


for i in range(M):
    ans = sys.stdin.readline().strip()
    if ans.isalpha():
        print(poke_dict[ans])
    else:
        print(poke_dict[int(ans)])
