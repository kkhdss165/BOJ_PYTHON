##최대 점수를 100점이 되어, 평균 구하기
##다른 점수들은 점수/최대점수 * 100
##평균 = 전체 점수 합/최대점수/과목수 * 100

n = int(input())

list = list(map(int, input().split()))
mx = max(list)
avg = sum(list) / mx / n * 100
print(avg)
