# 예제 7-5: 부품 찾기
n = int(input())
array = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

array.sort()

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return False

for t in targets:
    if binary_search(array, t, 0, n-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')