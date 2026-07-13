s='hello'

def reverse_string(s):

    stack = []


    for  i in s:
        stack.append(i)

    reversed = ""
    while stack:
        reversed+= stack.pop()
        
    return reversed

print(reverse_string(s))