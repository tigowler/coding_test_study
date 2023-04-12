# 정렬 라이브러리에서 key를 활용한 소스코드
# 176p
array = [('바나나', 2), ('사과', 5), ('당근', 3)]


def settings(data):
    return data[1]


result = sorted(array, key=settings)
print(result)
