a, b, c  = map(int, input().split())

##3개의 숫자가 모두 같을 때
if a == b and b == c:
  print(10000+a*1000)
##2개의 숫자만 같을 때
elif a == b:
  print(1000+a*100)
elif a == c:
  print(1000+a*100)
elif b == c:
  print(1000+b*100)
##같은 수가 없을 때
else:
  print(100*max(a,b,c))
