def heapify(arr, n, i):
    goc = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[goc]:
        goc = left

    if right < n and arr[right] > arr[goc]:
        goc = right

    if goc != i:
        arr[i], arr[goc] = arr[goc], arr[i]
        heapify(arr, n, goc)


def heap_sort(arr):
    n = len(arr)

    # Xây dựng Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Trích xuất phần tử tối đa và sắp xếp
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Danh sách đã được sắp xếp: ")
print(arr)
