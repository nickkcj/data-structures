#Can we get better than O(n log n)? 
#With non_comparison way sorts, we can! But it only works with integers in a specific range.
#Useful when we have numbers in a certain range.

#This algorithm sorts an array by counting the number of times each value occurs.

def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print(sortedArr) # [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]
