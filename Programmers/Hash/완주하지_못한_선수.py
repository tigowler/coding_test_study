# Programmers / Level 1
def solution(participant, completion):
    p_dict = {p: 0 for p in participant}
    for p in participant:
        p_dict[p] += 1

    for c in completion:
        p_dict[c] -= 1

    for key, value in p_dict.items():
        if value != 0:
            return key