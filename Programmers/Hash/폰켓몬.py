# Programmers / Level 1
def solution(nums):
    answer = 0
    monster_size = int(len(nums)/2)
    spieces_size = len(set(nums))
    return spieces_size if spieces_size <= monster_size else monster_size