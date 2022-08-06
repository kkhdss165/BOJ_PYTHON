#하노이 탑 이동 순서
#N <= 20
#N개의 원판들을 목적지로 옮길때, n-1개를 목적지가 아닌 곳으로 옮기고 n번째 원판을 목적지로 옮긴다
#1. N-1개 묶음을 목적지가 아닌곳으로 옯기고
#2. N번째 원판을 목적지로 옮기고
#3. N-1개 묶음을 목적지로 옮긴다
#1,2,3 기둥의 합은 6, 시작과 목적지가 아닌 기둥은 6-des-start

def hanoi(n, start, des):
  global count
  if n <= 1:
    print(start, des)
  else:
    hanoi(n-1, start, 6-des-start)
    print(start, des)
    hanoi(n-1, 6-des-start, des)

n = int(input())

print(2**n-1)
hanoi(n, 1, 3)
