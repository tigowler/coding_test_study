# Programmers / Level 2
def solution(phone_book):
    phone_dict = dict()
    for p in phone_book:
        for i in range(1, len(p)):
            phone_dict[p[:i]] = 1

    for p in phone_book:
        if p in phone_dict:
            return False
    return True