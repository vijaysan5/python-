## Stacks
# linear data structure that follows the Last-In-First-Out (LIFO) principle.
"""
Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
Size: Finds the number of elements in the stack."""

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# Size
print("Size: ",len(stack))

## Queues
# linear data structure that follows the First-In-First-Out (FIFO) principle.
"""
Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue."""

queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# Size
print("Size: ", len(queue))


