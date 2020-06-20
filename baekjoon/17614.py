# 완전 탐색 -> 시간초과
# N = int(input())
# rule = ['3', '6', '9']
# c = 0
# for i in range(1,N+1):
#     num = list(str(i))
#     for n in num:
#         if n in rule:
#             c += 1
# print(c)

N = list(input())
c = 0
pos = len(N)-1

for i in range(len(N)):
    n = int(N[i])
    d = 10**pos
    c1 = c2 = 0 

    c1 += (n//3)*d
    if (n%3 == 0) and (n != 0) and (i != len(N)-1):
        c1 -= d
        c1 += int(''.join(N[i+1:]))+1
    
    if i != 0:
        n_1 = int(''.join(N[:i]))
        c2 += (n_1)*3*d

    c += c1 + c2
    pos -= 1

print(c)