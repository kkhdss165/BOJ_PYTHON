#ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
#>> lj, e, s=, nj, a, k
#3개씩 탐색 -> 2개씩 탐색 -> 1개씩

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()
for i in cro_alpha:
  a = a.replace(i, '*')

print(len(a))
