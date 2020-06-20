import random

# 테스트 데이터 생성
def genData(s):
    b = []
    for i in range(s):
        r = random.randint(0,15)
        if r%2:
            b.append('R')
        else:
            b.append('B')
    return b

N = int(input())
balls = list(input())
# balls = genData(N)
# balls = ['R', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'B']
# print(N, balls)

redRblue = blueRred = redLblue = blueLred = 0
bc = rc = 0

# 빨강 왼쪽에 파랑 갯수
for ball in balls:
    if ball == 'B':
        bc += 1
    else:
        redLblue += bc
        bc = 0

# 파랑 왼쪽에 빨강 갯수
for ball in balls:
    if ball == 'R':
        rc += 1
    else:
        blueLred += rc
        rc = 0

bc = rc = 0
balls.reverse()
# 빨강 오른쪽에 파랑 갯수
for ball in balls:
    if ball == 'B':
        bc += 1
    else:
        redRblue += bc
        bc = 0

# 파랑 오른쪽에 빨강 갯수
for ball in balls:
    if ball == 'R':
        rc += 1
    else:
        blueRred += rc
        rc = 0

print(min([redRblue, redLblue, blueRred, blueLred]))

