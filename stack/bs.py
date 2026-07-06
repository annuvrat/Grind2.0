# Create a stack
stack = []

# Push items
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  # [10, 20, 30]

# Pop items (removes from the end)
top = stack.pop()
print(top)    # 30
print(stack)  # [10, 20]

# Peek at top
print(stack[-1])  # 20

# Check if empty
print(len(stack) == 0)  # False

# Size
print(len(stack))  # 2