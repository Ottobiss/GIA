# def f(s, m):
#     if s >= 58:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s + 1, m - 1), f(s + 4, m - 1), f(2 * s, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 58) if f(s, 2) and not (f(s, 0))])

'''-----------------------------------------------------'''

# def f(s, m):
#     if s >= 58:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s + 1, m - 1), f(s + 4, m - 1), f(2 * s, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 58) if f(s, 3) and not (f(s, 1))])

'''-----------------------------------------------------'''

# def f(s, m):
#     if s >= 58:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s + 1, m - 1), f(s + 4, m - 1), f(2 * s, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 58) if f(s, 4) and not (f(s, 2))])

'''-----------------------------------------------------'''

# def f(s, m):
#     if s >= 100:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s * 2, m - 1), f(s * 3, m - 1)]
#     return any(h)
#
#
# print([s for s in range(1, 100) if f(s, 2) and not (f(s, 0))])

'''-----------------------------------------------------'''

# def f(s, m):
#     if s >= 100:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s * 2, m - 1), f(s * 3, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 100) if f(s, 3) and not (f(s, 1))])

'''-----------------------------------------------------'''

# def f(s, m):
#     if s >= 100:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s * 2, m - 1), f(s * 3, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 100) if f(s, 4) and not (f(s, 2))])

'''-----------------------------------------------------'''

# def f(s, m):
#     if s >= 2163:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s + 1, m - 1), f(s * 3, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 2163) if f(s, 2) and not (f(s, 0))])

'''-----------------------------------------------------'''

# def f(s, m):
#     if s >= 2163:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [f(s + 1, m - 1), f(s * 3, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 2163) if f(s, 4) and not (f(s, 2))])

'''-----------------------------------------------------'''

# def f(s1, s2, m):
#     if s1 == s2:
#         return m % 2 == 0
#     if abs(s1 - s2) == 2:
#         return (m - 2) % 2 == 0
#     if abs(s1 - s2) <= 3:
#         return (m - 1) % 2 == 0
#     if m == 0:
#         return False
#     if s1 < s2:
#         h = [f(s1 + 1, s2, m - 1), f(s1 + 3, s2, m - 1)]
#     else:
#         h = [f(s1, s2 + 1, m - 1), f(s1, s2 + 1, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 24) if f(13, s, 2) and not (f(13, s, 0))])

'''-----------------------------------------------------'''

# def f(s1, s2, m):
#     if s1 == s2:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     if abs(s1 - s2) == 2:
#         return (m - 2) % 2 == 0
#     if abs(s1 - s2) <= 3:
#         return (m - 1) % 2 == 0
#     if s1 < s2:
#         h = [f(s1 + 1, s2, m - 1), f(s1 + 3, s2, m - 1)]
#     else:
#         h = [f(s1, s2 + 1, m - 1), f(s1, s2 + 3, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 24) if f(13, s, 3) and not (f(13, s, 1))])

'''-----------------------------------------------------'''

# def f(s1, s2, m):
#     if s1 == s2:
#         return m == 0
#     if m == 0:
#         return False
#     if abs(s1 - s2) == 2:
#         return (m - 2) == 0
#     if abs(s1 - s2) <= 3:
#         return (m - 1) == 0
#     if s1 < s2:
#         h = [f(s1 + 1, s2, m - 1), f(s1 + 3, s2, m - 1)]
#     else:
#         h = [f(s1, s2 + 1, m - 1), f(s1, s2 + 3, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 24) if f(13, s, 4) and not (f(13, s, 2))])

'''-----------------------------------------------------'''

# def f(s1, s2, m):
#     if s1 + s2 == 13:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     if s1 + s2 < 12:
#         h = [f(s1+1, s2, m-1), f(s1+2, s2, m-1), f(s1, s2+1, m-1), f(s1, s2+2, m-1)]
#     else:
#         h = [f(s1 + 1, s2, m - 1),  f(s1, s2 + 1, m - 1)]
#     return any(h)
#
#
# print([s for s in range(1, 10) if f(3, s, 2) and not (f(3,s,0))])

'''-----------------------------------------------------'''

# def f(s1, s2, m):
#     if s1 + s2 == 13:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     if s1 + s2 < 12:
#         h = [f(s1 + 1, s2, m - 1), f(s1 + 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 + 2, m - 1)]
#     else:
#         h = [f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 10) if f(3, s, 3) and not (f(3, s, 1))])

'''-----------------------------------------------------'''

# def f(s1, s2, m):
#     if s1 + s2 == 13:
#         return m == 0
#     if m == 0:
#         return False
#     if s1 + s2 < 12:
#         h = [f(s1 + 1, s2, m - 1), f(s1 + 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 + 2, m - 1)]
#     else:
#         h = [f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print([s for s in range(1, 10) if f(3, s, 4) and not (f(3, s, 2))])

'''-----------------------------------------------------'''


def f(s1, s2, m):
    if (s1 == 0 or s2 == 0) or ((s1 == 1 and s2 % 2 != 0) or (s2 == 1 and s1 % 2 != 0)):
        return m % 2 == 0
    if m == 0:
        return False
    h = []
    if s1 >= 3 and s2 >= 3:
        h.append(f(s1 - 3, s2 - 3, m - 1))
    if s1 % 2 == 0:
        h.append(f(s1//2, s1//2, m - 1))
    if s2 % 2 == 0:
        h.append(f(s2//2, s2//2, m - 1))
    return any(h) if m % 2 != 0 else all(h)


print([s for s in range(1, 1000) if f(20, s, 4) and not (f(20, s, 0))])

