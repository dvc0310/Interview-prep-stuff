class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if self.stack:
            x = self.stack.pop()
            if x == self.max_stack[-1]:
                self.max_stack.pop()
            return x
        return None

    def max(self):
        return self.max_stack[-1] if self.max_stack else None

def main():
    stack = MaxStack()

    # Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(2)
    print(f"Max element: {stack.max()}")  # Output: Max element: 3

    # Pop elements from the stack
    print(f"Popped element: {stack.pop()}")  # Output: Popped element: 2
    print(f"Max element: {stack.max()}")  # Output: Max element: 3

    print(f"Popped element: {stack.pop()}")  # Output: Popped element: 3
    print(f"Max element: {stack.max()}")  # Output: Max element: 2

    # Push another element onto the stack
    stack.push(4)
    print(f"Max element: {stack.max()}")  # Output: Max element: 4

    # Pop all remaining elements
    while stack.max() is not None:
        print(f"Popped element: {stack.pop()}, Max element: {stack.max()}")

# Run the main function
if __name__ == "__main__":
    main()

