# m = 2
# data = [[] for _ in range(m)]
#
#
# def dist(point1, point2):
#     return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
#
#
# for s in open('27_task_A_1.txt'):
#     x, y = map(float, s.replace(',', '.').split())
#     if y > 6:
#         data[0].append((x, y))
#     else:
#         data[1].append((x, y))
#
# sum_dist = [[] for _ in range(m)]
# centers = []
#
# for i in range(m):
#     for p1 in data[i]:
#         sum_dist[i].append((sum(dist(p1, p2) for p2 in data[i]), p1))
#     centers.append(min(sum_dist[i])[1])
#
# print(int(abs(sum(cl[0]*10000/m for cl in centers))), int(abs(sum(cl[1]*10000/m for cl in centers))))

'''------------------------------------------------------------------------------------'''

# m = 3
# data = [[] for _ in range(m)]
#
#
# def dist(point1, point2):
#     return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
#
#
# for s in open('27_task_B_1.txt'):
#     x, y = map(float, s.replace(',', '.').split())
#     if x < 0:
#         data[0].append((x, y))
#     elif y < 7:
#         data[1].append((x, y))
#     else:
#         data[2].append((x, y))
#
# sum_dist = [[] for _ in range(m)]
# centers = []
#
# for i in range(m):
#     for p1 in data[i]:
#         sum_dist[i].append((sum(dist(p1, p2) for p2 in data[i]), p1))
#     centers.append(min(sum_dist[i])[1])
#
# print(int(abs(sum(cl[0]*10000/m for cl in centers))), int(abs(sum(cl[1]*10000/m for cl in centers))))

'''------------------------------------------------------------------------------------'''

# m = 3
# data = [[] for _ in range(m)]
#
#
# def dist(point1, point2):
#     return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
#
#
# for s in open('27_task_A_2.txt'):
#     x, y = map(float, s.replace(',', '.').split())
#     if y > 6:
#         data[0].append((x, y))
#     elif x < 4:
#         data[1].append((x, y))
#     else:
#         data[2].append((x, y))
#
# sum_dist = []
#
# for i in range(m):
#     if len(data[i]) >= 361:
#         sum_dist.append([])
#         for p1 in data[i]:
#             sum_dist[-1].append((sum(dist(p1, p2) for p2 in data[i]), p1))
#
# centers = [min(x)[1] for x in sum_dist]
#
# print(int(sum(p[0]/len(centers) for p in centers)*100000), int(sum(p[1]/len(centers) for p in centers)*100000))

'''------------------------------------------------------------------------------------'''

m = 6
data = [[] for _ in range(m)]


def dist(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


for s in open('27_task_B_2.txt'):
    x, y = map(float, s.replace(',', '.').split())
    if y > 8.9:
        data[5].append((x, y))
    elif y < (-2*x + 7):
        data[0].append((x, y))
    elif y > (x/3) + 4 and x < 3.6:
        data[1].append((x, y))
    elif y > (x/3) + 4 and x > 3.6:
        data[2].append((x, y))
    elif y < (x/3) + 4 and x > 5:
        data[3].append((x, y))
    else:
        data[4].append((x, y))

sum_dist = []

for i in range(m):
    if len(data[i]) >= 1706:
        sum_dist.append([])
        for p1 in data[i]:
            sum_dist[-1].append((sum(dist(p1, p2) for p2 in data[i]), p1))

centers = [min(x)[1] for x in sum_dist]

print(int(sum(p[0]/len(centers) for p in centers)*100000), int(sum(p[1]/len(centers) for p in centers)*100000))
