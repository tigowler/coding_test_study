# 위에서 아래로
# 178p
n = int(input())
array = [int(input()) for _ in range(n)]
array.sort(reverse=True)
for a in array:
    print(a, end=' ')