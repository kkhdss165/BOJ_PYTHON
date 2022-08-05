#평균을 구하고 평균을 넘는 비율 구하기
testcase = int(input())

for i in range(testcase):
    list1 = list(map(int, input().split()))
    avg = sum(list1[1:]) / list1[0]
    #평균보다 큰 점수들 리스트
    list2 = []
    for j in range(list1[0]):
        if list1[j + 1] > avg:
            list2.append(list1[j + 1])
    per = len(list2) / (len(list1) - 1) * 100
    print('%.3f' % per + '%')
