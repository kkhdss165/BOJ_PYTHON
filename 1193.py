#X번째 분수 구하기
#1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#1~1 : 합 2(1 +1) > 1열(count)
#2~3 : 합 3(1+2 +1) > 2열
#4~6 : 합 4(1+2+3 +1) > 3열
#5의 경우: 3열 2행으로 정의 2/2(합:4, 순서:2)
#지그재그 순서...(홀수 짝수)

n = int(input())
count = 0
start = 0
end = 0
while True:
  if n <= end :
    break
  else:
    count = count + 1
    start = end + 1
    end = end + count
    
front, back = None, None
if count % 2 == 0:
  front = n - start + 1
else:
  front = end - n + 1
back = (count + 1) - front
print(str(front)+"/"+str(back))
