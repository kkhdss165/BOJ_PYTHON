#평균, 중앙값, 최빈값, 범위 구하기
import sys
from collections import Counter
N = int(sys.stdin.readline())
values =[]

for i in range(N):
    x = int(sys.stdin.readline())
    values.append(x)

#평균
print(round(sum(values)/N))
#중앙값
values.sort()
print(values[N//2])
#최빈값
result = None
counts = Counter(values).most_common()
if len(counts) == 1:
    result = counts[0][0]
elif counts[0][1] == counts[1][1]:
    result = counts[1][0]
else:
    result = counts[0][0]
print(result)
#범위
print(values[-1]-values[0])
