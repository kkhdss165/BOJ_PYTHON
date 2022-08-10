# 직사각형에서 탈출 1085
# https://www.acmicpc.net/problem/1085
# 첫째 줄에 x, y, w, h가 주어진다.
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

x, y, w, h = map(int, input().split())

print(min(x,w-x, y, h-y))
