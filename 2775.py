##“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
## 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
## 재귀함수

def house(floor, room):
  if (floor == 0):
    return room
  else:
    sum = 0
    for i in range(1,room+1):
      sum = sum + house(floor-1, i)
    return sum

testCase = int(input())
for t in range(testCase):
  floor = int(input())
  room = int(input())
  print(house(floor,room))
