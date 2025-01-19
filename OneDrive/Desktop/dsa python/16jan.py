def get_index(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            arr.pop(mid)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 6, 7, 8, 9]
target = 6
result = get_index(arr, target)
print("Index:", result)
print("Result:", arr)
