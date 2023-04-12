# 성적이 낮은 순대로 학생 출력하기
# 180p
n = int(input())
array = []
for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))

# array.sort(key=lambda student : student[1])


def setting(data):
    return data[1]


array.sort(key=setting)
for a in array:
    print(a[0], end=' ')