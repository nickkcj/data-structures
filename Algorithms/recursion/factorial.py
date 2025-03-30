#Recursion is when you define something in terms of itself
def findFactorialRecursive(number):
    #Base case
    if number == 0 or number == 1:
        return 1
    
    return number * findFactorialRecursive(number - 1)


#Iterative is when you use a loop to do the same thing
def findFactorialIterative(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
