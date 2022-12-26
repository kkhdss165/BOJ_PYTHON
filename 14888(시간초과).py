# 코테연습 14888
# 연산자 끼워넣기
# 입력은 3번째 줄을
# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
## 시간초과

_ = input()
num_list = list(map(int, input().split()))
oper_num = list(map(int, input().split()))

oper_list = ['더하기']*oper_num[0]+['빼기']*oper_num[1]+ ['곱하기']*oper_num[2]+['나누기']*oper_num[3]
#print(oper_list)

used_oper = []
results = []
def cal():
    result = num_list[0]
    for i in range(len(used_oper)):
        if used_oper[i] == '더하기':
            result += num_list[i+1]

        elif used_oper[i] == '빼기':
            result -= num_list[i+1]

        elif used_oper[i] == '곱하기':
            result *= num_list[i+1]

        ## 나누기
        elif  used_oper[i] == '나누기':
            result = int(result / num_list[i+1])

    return result



def DFS(index):
    if index == len(num_list)-1:
        #계산
        # print(used_oper, cal())
        result = cal()
        if result not in results:
            results.append(result)
        return

    else:
        for oper in oper_list:
            # print(oper, used_oper.count(oper), oper_list.count(oper))
            if used_oper.count(oper) < oper_list.count(oper):
                used_oper.append(oper)
                DFS(index+1)
                used_oper.pop()

DFS(0)
print(max(results))
print(min(results))
