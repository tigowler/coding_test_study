# 예제 7-8: 떡볶이 떡 만들기
n, m = map(int, input().split())
cakes = list(map(int, input().split()))
res = -1


def calc_height(arr, height):
    s = 0
    for a in arr:
        r = a-height
        s = s + r if r > 0 else s
    return s


def binary_search(array, start, end):
    global res
    while start<=end:
        mid = (start+end)//2
        h = calc_height(array, mid)
        if h >= m: # m 이상의 길이를 얻은 경우
            res = mid if res<mid else res # 최댓값 확인 및 변경/유지
            start = mid+1
        else: # m 미만인 경우, 설정 길이를 줄여야 함
            end = mid-1


binary_search(cakes, 0, max(cakes))
print(res)

