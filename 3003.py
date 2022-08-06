#체스말의 갯수 맞추기
#킹, 퀸, 룩, 비숍, 나이트, 폰 순으로
#(1, 1, 2, 2, 2, 8) 맞추기

list = list(map(int, input().split()))
true_values = [1, 1, 2, 2, 2, 8]

for i in range(len(list)):
  print(true_values[i] - list[i], end=" ")
