#피보나치 수열 (N>=2)
#점화식
N = int(input())

fibo = [-1] * (N+1)
fibo[0] = 0

for i in range(1, N+1):
  if i == 1:
    fibo[1] = 1
  else:
    fibo[i] = fibo[i-2] + fibo[i-1]

print(fibo[N])
