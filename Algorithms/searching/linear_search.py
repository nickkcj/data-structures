def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return None

# Example usage
numbers = [1, 2, 3, 4, 5]
target = 3
result = linear_search(numbers, target)
if result is not None:
    print(f"Element found at index {result}.")