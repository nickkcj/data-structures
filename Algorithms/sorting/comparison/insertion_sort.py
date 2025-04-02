#Not the best sorting algorithm but there are cases where it is extremely fast
#It performs really well with small data sets
#Just like bubble and selection sort, it is O(n^2) (really bad), but with a space complexity of O(1)

def insertionSort(arr):
  n = len(arr)
  if n <= 1:
    return arr
    
  for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
 

arr = [12, 11, 13, 5, 6]
print(insertionSort(arr)) # [5, 6, 11, 12, 13]


  
  
