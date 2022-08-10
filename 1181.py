#단어 정렬
#1.길이가 짧은 것부터
#2.길이가 같으면 사전 순으로
#중복 X

N = int(input())
values = []

for i in range(N):
    values.append(input())

values = list(set(values))
values.sort()
values.sort(key=lambda x:len(x))

for word in values:
    print(word)
