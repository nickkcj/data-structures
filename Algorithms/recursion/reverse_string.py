def reverseStringRecursive(string):
    #Base case
    if len(string) <= 1:
        return string
    
    return string[-1] + reverseStringRecursive(string[:-1])

print(reverseStringRecursive("Hello World")) #dlroW olleH


def reverseStringIterative(string):
    #Base case
    if len(string) <= 1:
        return string
    
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

print(reverseStringIterative("Python")) #nohtyP