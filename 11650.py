#좌표 정렬
#좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로
#y좌표 정렬하고 x좌표 정렬하면 됨

N = int(input())

points =[]
for i in range(N):
    x, y = map(int,input().split())
    points.append((x,y))

# points.sort(key = lambda x : x[1])
# points.sort(key = lambda x : x[0])
points.sort(key = lambda x : (x[0],x[1]))

for point in points:
    print(point[0],point[1])
