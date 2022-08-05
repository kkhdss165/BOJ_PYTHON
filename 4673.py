#생성자가 없는 수 = 셀프넘버
list = []
max_range = 10000
for n in range(1, max_range):
    n_str = str(n)
    for i in n_str:
        n = n + int(i)
    if n not in list:
        #생성자가 있는 수 추가(셀프넘버 아님)
        list.append(n)

for i in range(1, max_range):
    if i not in list:
        print(i)
