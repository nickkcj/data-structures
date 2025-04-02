#HARD TO IMPLEMENT
#Why? Cause this sorting method uses Divide and Conquer (another Algorithm), which leaves us with O(n log n)!

#Divide and Conquer: Divide and Conquer Algorithm is a problem-solving technique used to solve problems by dividing 
#the main problem into subproblems, solving them individually and then merging them to find solution to the original problem. 
#Divide and Conquer is mainly useful when we divide a problem into independent subproblems.

def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]

size = len(data)

quickSort(data, 0, size - 1)

print(data) # [-2, 1, 1, 4, 7, 9, 10]
