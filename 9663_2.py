# 코테연습 9663
N = int(input())

count = 0

values = []

## 대각선 체크
def check(list, new_element):
    insert_n = len(list) + 1
    if insert_n == 1:
        return True
    else:
        for i in range(1, insert_n):
            ##가로 차이
            diff_x = i - insert_n
            ##세로 차이
            diff_y = list[i-1] - new_element

            if abs(diff_y) == abs(diff_x):
                return False
        return True


## 같은 직선상에 없게 해놓음
def DFS():
    global count
    if len(values) == N:
        # print(*values)
        count += 1
        return
    else:
        for i in range(1, N+1):
            if i not in values and check(values, new_element = i):
                values.append(i)
                DFS()
                values.pop()

DFS()
print(count)
