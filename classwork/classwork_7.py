# s = open('7_task.txt').readline().strip()
#
# k = mx = 0
#
# for i in range(len(s)):
#     if (s[i] == '0' and k > 0) or ('0' < s[i] <= 'F'):
#         k += 1
#         mx = max(mx, k)
#     else:
#         k = 0
#
# print(mx)

'''---------------------------------------------------------------------'''
import re

# import re
#
# s = open('7_task_1.txt').readline().strip()
#
# num = r'(?:[1-9][0-9]*[05]|[05])'
# aref = rf'{num}(?:[+*]{num})*'
#
# regs = max(re.findall(aref, s), key=len)
# print(len(regs))

'''---------------------------------------------------------------------'''

# s = open('7_task_2.txt').readline().strip()
#
# k = mx = 3
#
# for i in range(3, len(s)-1):
#     if (s[i] in 'CDF' and s[i-1] in 'AO' and s[i-2] in 'AO' and s[i-3] in 'CDF'):
#         k = 3
#     else:
#         k += 1
#         mx = max(mx, k)
#
# print(mx)

'''---------------------------------------------------------------------'''

# s = open('7_task_3.txt').readline().strip()
#
# k = mx = 1
#
# for i in range(1, len(s)):
#     if s[i] in 'QRS' and s[i-1] in 'QRS':
#         k = 1
#     else:
#         k+=1
#         mx = max(mx, k)
#
# print(mx)

'''---------------------------------------------------------------------'''

# s = open('7_task_4.txt').readline().strip()
#
# xc = 0
#
# mn = float('inf')
# lt = 0
#
# for rt in range(0, len(s)):
#     if s[rt] == 'Y':
#         lt = rt + 1
#         xc = 0
#     if s[rt] == 'X':
#         xc += 1
#     while xc == 500:
#         mn = min(mn, rt - lt + 1)
#         if s[lt] == 'X':
#             xc -= 1
#         lt += 1
#
# print(mn)

'''---------------------------------------------------------------------'''

# s = open('7_task_5.txt').readline().strip()
#
# num = r'(?:[1-5][0-5]*|0)'
# aref = rf'{num}(?:[+*]{num})*'
#
# mn = max(re.findall(aref, s), key=len)
# print(len(mn))

'''---------------------------------------------------------------------'''

# s = open('7_task_6.txt').readline().strip()
#
# mx = 0
#
# roc = 0
#
# lt = 0
#
# for rt in range(1, len(s)):
#     if (s[rt - 2:rt + 1] == 'ORO') or (s[rt - 2:rt + 1] == 'ROR'):
#         lt = rt - 1
#         roc = 0
#     if s[rt - 1:rt + 1] == 'RO':
#         roc += 1
#     while roc > 21:
#         if s[lt:lt + 2] == 'RO':
#             roc -= 1
#         lt += 1
#     if roc == 21:
#         mx = max(mx, rt - lt + 1)
#
# print(mx)

'''---------------------------------------------------------------------'''

# s = open('7_task_7.txt').readline().strip()
#
# mx = 0
#
# for i in range(2):
#     k = 0
#     for j in range(i, len(s) - 1, 2):
#         if s[j] in 'AC' and s[j + 1] == 'B':
#             k += 1
#             mx = max(mx, k)
#         else:
#             k = 0
#
# print(mx)

'''---------------------------------------------------------------------'''

s = open('7_task_8.txt').readline().strip()

mx = 0

for i in range(2):
    k = 0
    for j in range(i, len(s) - 1, 2):
        if s[j] in 'AC' and s[j] == s[j+1]:
            k += 1
            mx = max(mx, k)
        else:
            k = 0
print(mx)
