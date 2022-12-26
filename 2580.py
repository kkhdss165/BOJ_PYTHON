# 코테연습 2580
# 스도쿠
element_list = []
zero_pos = []
for i in range(9):
    sub_list = list(map(int, input().split()))
    element_list.append(sub_list)
    for idx,value in enumerate(sub_list):
        if value == 0:
            zero_pos.append((i,idx))

def print_list():
    print()
    for e in element_list:
        print(*e)

def row_check(row, new_element):
    if new_element not in element_list[row]:
        return True
    else:
        return False

def col_check(col, new_element):
    col_list = [i[col] for i in element_list]
    if new_element not in col_list:
        return True
    else:
        return False

def box_check(row, col, new_element):
    row_start = row//3 * 3
    col_start = col//3 * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if element_list[r][c] == new_element:
                return False

    return True

## 가로줄에 대해서만 체크후 DFS
def DFS(index):
    if index == len(zero_pos):
        print_list()
        exit(0)
    else:
        pos = zero_pos[index]
        row = pos[0]
        col = pos[1]
        for i in range(1, 10):
            if row_check(row, i) and col_check(col, i) and box_check(row,col,i):
                element_list[pos[0]][pos[1]] = i
                DFS(index+1)
                element_list[pos[0]][pos[1]] = 0


# print_list()

# print(zero_pos)


DFS(0)
# print_list()
