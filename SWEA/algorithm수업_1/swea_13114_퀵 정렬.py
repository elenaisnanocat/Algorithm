# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램

def quick_sort(s,e):
    if s >= e:
        return

    pivot = arr[s]
    left = s + 1
    right = e

    while left <= right:
        while left <= right and arr[left] <= pivot:
            left += 1
        while s < right and arr[right] >= pivot:
            right -= 1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]

    arr[s],arr[right] = arr[right],arr[s]

    quick_sort(s, right -1)
    quick_sort(right+1, e)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    quick_sort(0,N-1)

    print('#{} {}'.format(tc,arr[N//2]))