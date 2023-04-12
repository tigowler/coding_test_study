# Programmers / Level 2
def solution(clothes):
    _dict = {value:[] for key,value in clothes}

    for key, value in clothes:
        _dict[value].append(key)

    answer = 1
    for value in _dict.values():
        answer *= (len(value)+1)

    return answer - 1