#나이순 정렬(10814)
#회원들을 나이가 증가하는 순으로
#나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    members.append((i, int(age), name))

members.sort(key=lambda x: (x[1],x[0]))

for member in members:
    print(member[1], member[2])
