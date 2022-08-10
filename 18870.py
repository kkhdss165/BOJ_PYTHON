#좌표압축(18870)
# https://www.acmicpc.net/problem/18870
# Xi를 좌표 압축한 결과 Xi의 값은
# Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# set함수로 중복을 제거하고 정렬을 하면 그 인덱스의 값이 자신보다 작은 좌표의 갯수이다

import sys

N = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split()))

set_points = list(set(points))
set_points.sort()

dic = {set_points[i]:i for i in range(len(set_points))}

for point in points:
    print(dic[point], end = " ")
