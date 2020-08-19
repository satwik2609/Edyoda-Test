class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)

        if len(self.main_stack) == 1:
            self.max_stack.append(data)
        elif data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    def maximum(self):
        return self.max_stack[-1]

s = MaxStack()
n = int(input("Enter number of commands: "))
for i in range(n):
    c = input().split()
    if c[0] == 'push':
        s.push(c[1])
    elif c[0] == 'pop':
        s.pop()
    elif c[0] == "max":
        print(s.maximum())