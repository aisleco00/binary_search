def binary_search(arr, num):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == num:
            found = True
        else:
            if num < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print('Binary Search:', binary_search(arr, 11))
print('Binary Search:', binary_search(arr, 25))
print('Binary Search:', binary_search(arr, 2))
