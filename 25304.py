#영수증 가격 확인
#전체 물건의 가격의 합이 총합과 맞으면 Yes, 틀리면 No

X = int(input())
testCase = int(input())
total = 0
for t in range(testCase):
  a, b = map(int, input().split())
  total = total + a * b

if total == X : 
  print("Yes")
else:
  print("No")
