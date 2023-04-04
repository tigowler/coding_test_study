# 예제 4-3: 왕실의 나이트
# 115p
s = input()
x = ord(s[0]) - 96
y = int(s[1])
dirx = [-1, 1, -1, 1, -2, -2, 2, 2]
diry = [-2, -2, 2, 2, -1, 1, -1, 1]
count = 0

for i in range(len(dirx)):
    nx = x + dirx[i]
    ny = y + diry[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)
