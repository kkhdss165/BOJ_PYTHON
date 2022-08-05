#벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지
#1일때는 1
#2~7 일때는 2 (1+6) >> 6*0+2 ~ 6*1+1
#8~19 일때는 3 (1+6+12) >>  6*1+2 ~ 6*3+1
#20~37 일때는 4 (1+6+12+18) >> 6*3+2 ~ 6*6+1
#n일때 몇개의 방을 지나는지?? (N ≤ 1,000,000,000)

n = int(input())
start = -1
end = 0
count = 1
while True:
  if  n >= 6 * start + 2 and n <= 6 * end + 1:
    break
  else:
    start = end
    end = end + count
    count = count + 1
    
print(count)
