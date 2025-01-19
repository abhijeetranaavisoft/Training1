def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example usage
arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sort_012(arr))

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))


def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

# Example usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))


def count_pairs_with_sum(arr, target):
    count = 0
    freq = {}
    for num in arr:
        complement = target - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1
    return count

# Example usage
arr = [1, 5, 7, 1, 5]
target = 6
print(count_pairs_with_sum(arr, target))



def minimize_tower_heights(arr, k):
    arr.sort()
    n = len(arr)
    min_diff = arr[-1] - arr[0]
    for i in range(1, n):
        min_height = min(arr[0] + k, arr[i] - k)
        max_height = max(arr[i - 1] + k, arr[-1] - k)
        min_diff = min(min_diff, max_height - min_height)
    return min_diff

# Example usage
arr = [1, 5, 8, 10]
k = 2
print(minimize_tower_heights(arr, k))
