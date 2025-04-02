def binary_search(arr, target):
    # Keep dividing the array into halves until the target is found or the search space is empty.
    # The array must be sorted for binary search to work correctly.
    # The complexity of binary search is O(log n) in the average and worst case.
    # The space complexity is O(1) since we are not using any additional data structures.
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

#Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(numbers, target)
if result != -1:
    print(f"Element found at index {result}.")