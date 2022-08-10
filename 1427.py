#첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

N = input()
values = []
for i in N:
    values.append(int(i))

values.sort(reverse=True)
for i in values:
    print(i, end="")
