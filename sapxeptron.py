def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # tìm phần tử ở giữa
        L = arr[:mid]  # chia đôi phần tử giữa ra 2 bên
        R = arr[mid:]

        mergeSort(L)  #sắp xếp 2 bên
        mergeSort(R)

        i = j = k = 0

        # so sánh phần tử với mỗi ptu trong phía của nó
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # kiểm tra phần tử bên trái hay chưa
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):# kiểm tra phần tử bên phải hay chưa
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
