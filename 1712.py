## A = 1000 B = 70 C = 170
## A 고정 비용 B 가변 비용 C 판매비용
## n이 언제일때 n * C > n * B + A 가 성립하냐
## n= 11:  n * C (1870)> n * B + A(1770)
## 제한시간 0.35초 이므로 대입이 아니라 계산
## n > A/(C-B)
## B > C 일때는 이익이 발생하지 않으므로 -1

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    #같아질 때 n에서 1더하기
    n = A / (C - B) + 1
    print(int(n))
