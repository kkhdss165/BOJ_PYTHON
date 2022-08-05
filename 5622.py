#UNUCIC는 868242
#WA는 92(sum:10) -> 13초
#UNUCIC 868242(sum:30) -> 36초
#문자 위치 + 1만큼 시간이 걸림

dial = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
time = 0
for i in a:
    for index, d in enumerate(dial):
        if i in d:
            time = time + (index + 1)

print(time)
