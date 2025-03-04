# import fnmatch
#
# spis = []
#
# for x in range(596, 10 ** 12 + 1, 596):
#     if fnmatch.fnmatch(str(x), '1*28?64'):
#         spis.append(x)
#
# print(len(spis), sum(spis) // len(spis))

# import itertools
#
# spis_ch = []
# spis_shs = ['']
#
# for i in range(1, 7):
#     for s in map(''.join, itertools.product('0123456789', repeat=i)):
#         spis_shs.append(s)
#
# for i in spis_shs:
#     for j in '0123456789':
#         x = int(f'1{i}28{j}64')
#         if x % 596 == 0:
#             spis_ch.append(x)
#
# print(len(spis_ch), sum(spis_ch) // len(spis_ch))

# import fnmatch
#
# for x in range(211, 10**8+1, 211):
#     if fnmatch.fnmatch(str(x), '11??4*56'):
#         print(x, x//211)

'''------------------------------------------------'''


# def f(x):
#     m = set()
#     for s in range(1, int(x**0.5) + 1):
#         if x % s == 0:
#             m.add(s)
#             m.add(x//s)
#     return sorted(m)
#
# counter = 0
#
# for ch in range(55000001, 10**10):
#     dels = f(ch)[:-1]
#     dels_2 = [x for x in dels if x%1000==777 and len(f(x))==2]
#     if dels_2:
#         counter += 1
#         print(ch, dels_2[0])
#         if counter == 4:
#             break

# def f(x):
#     m = set()
#     for s in range(1, int(x ** (1 / 2)) + 1):
#         if x % s == 0:
#             m.add(s)
#             m.add(x // s)
#     return sorted(m)
#
#
# counter = 0
#
# for ch in range(32500001, 10 ** 10):
#     dels = f(ch)[:-1]
#     s = sum([x for x in dels if len(f(x)) == 2])
#     if s != 0 and s % 145 == 0:
#         counter += 1
#         print(ch, s)
#         if counter == 7:
#             break

# def f(x):
#     m = set()
#     for s in range(1, int(x**(1/2))+1):
#         if x % s == 0:
#             m.add(s)
#             m.add(x//s)
#     return sorted(m)
#
# counter = 0
#
# for ch in range(10**8+2, 10**10, 2):
#     dels = f(ch)
#     dels_pr = [x for x in dels if len(f(x))==2]
#     dels_c = [x for x in dels if x%2 == 0]
#
#     if len(dels_c) == len(dels_pr):
#         counter += 1
#         print(ch, abs(sum(dels_pr) - sum(dels_c)))
#         if counter == 5:
#             break

def f(x):
    m = set()
    for s in range(1, int(x ** (1 / 2)) + 1):
        if x % s == 0:
            m.add(s)
            m.add(x // s)
    return sorted(m)


for ch in range(333555, 778000):
    dels = [x for x in f(ch) if 9 < x < 100]
    if len(dels) == 35:
        print(dels[0], dels[-1])
