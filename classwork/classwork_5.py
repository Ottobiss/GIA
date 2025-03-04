# def t(x):
#     return 9999<abs(x)<=99999 and abs(x) % 100 == 43
#
# spis = []
#
# with open('data.txt') as f:
#     a = [int(x) for x in f]
#     mx = max([x for x in a if t(x)])
#     for x, y, z in zip(a, a[1:], a[2:]):
#         if (t(x) or t(y) or t(z)) and (x**2 + y**2 + z**2) <= mx**2:
#             spis.append(x**2 + y**2 + z**2)
#
# print(len(spis), min(spis))

'''-----------------------------------------------------'''
# def t(x, y):
#     return x == y
#
# spis = []
#
# with open('data.txt') as f:
#     a = [int(x) for x in f]
#     m6 = min([x for x in a if 6 ** 3 <= x < 6 ** 4]) % 5
#     m9 = min([x for x in a if 9 ** 2 <= x < 9 ** 3]) % 13
#     for x, y, z in zip(a, a[1:], a[2:]):
#         if (t(x%11, m6) + t(y%11, m6) + t(z%11, m6)) == 1:
#             if (t(x % 7, m9) + t(y % 7, m9) + t(z % 7, m9)) == 1:
#                 spis.append(x + y + z)
#
# print(len(spis), min(spis))
'''-----------------------------------------------------'''
# def t(x, y):
#     return x == y
#
# spis = []
#
# with open('data.txt') as f:
#     a = [int(x) for x in f]
#     maxi = max(a) % 11
#     mini = min(a) % 3
#     for x, y, z in zip(a, a[1:], a[2:]):
#         if (t(x%3, maxi) + t(y%3, maxi) + t(z%3, maxi)) == 1:
#             if (t(x % 11, mini) + t(y % 11, mini) + t(z % 11, mini)) == 1:
#                 spis.append(x + y + z)
#
# print(len(spis), min(spis))
'''-----------------------------------------------------'''
# def t(x):
#     return x%10==2
#
# spis = []
#
# with open('data.txt') as f:
#     a = [int(x) for x in f]
#     maxi = max([x for x in a if x % 10 == 3])
#     for x, y, z, w in zip(a, a[1:], a[2:], a[3:]):
#         if (t(x) + t(y) + t(z) + t(w))%2 and max([x, y, z, w]) < maxi:
#             spis.append(x + y + z + w)
#
# print(len(spis), min(spis))
'''-----------------------------------------------------'''
# def t(x):
#     return 1000 <= abs(x) <= 9999 and abs(x) % 10 == 7
#
#
# spis = []
#
# with open('data.txt') as f:
#     a = [int(x) for x in f]
#     maxi = max([x for x in a if t(x)])
#     for x, y, z in zip(a, a[1:], a[2:]):
#         if t(x) + t(y) + t(z) >= 2 and (x + y + z) > maxi:
#             spis.append(x + y + z)
#
# print(len(spis), max(spis))
'''-----------------------------------------------------'''


def t(x, y):
    return x < 0 or y < 0


spis = []

with open('data.txt') as f:
    a = [int(x) for x in f]

    c = len([x for x in a if x % 32 == 0])

    for x, y in zip(a, a[1:]):
        if t(x, y) and x + y < c:
            spis.append(x + y)

print(len(spis), max(spis))
