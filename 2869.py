#달팽이
#하루 A만큼 올라가고 B만큼 내려감 C까지 걸리는 시간(일)
#A:2 B:1 C:5 -> 4일
#n일차일때 거리의 범위 A*n-B*n ~ A*n-B*(n-1)
#제한시간 때문에 계산해야됨

import sys
import math
A, B, C = map(int, sys.stdin.readline().split())

#(C-B) : 정상에 도달했을때 미끄러지지 않은것 을 가정한 거리
#(A-B) : 하루 갈 수 있는 거리
day = (C-B)/(A-B)
print (math.ceil(day))
