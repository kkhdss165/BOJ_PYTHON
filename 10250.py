##6 12 10 6개의층 12호까지
##나머지와 몫을 이용하여
import sys

testCase = int(sys.stdin.readline())
for t in range(testCase):
  H, W, N = map(int, sys.stdin.readline().split())
  floor = N%H
  if floor == 0:
    floor = H
  ho = int((N-1)/H) + 1
  print(str(floor)+str(ho).zfill(2))
