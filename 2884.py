h, m  = input().split()

##입력받은 시간을 전체 분으로 변환후 45분 빼서 다시 시간:분으로
total = int(h) * 60 + int(m) + 1440
total = (total - 45) % 1440
result_h = total // 60
result_m = total % 60
print(result_h,result_m)
