class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    # Last in First Out
    def push(self, data):
        if self.top + 1 >= self.size:
            print("Stack overflow....")
            return
        self.stack.append(data)
        self.top = self.top + 1

    def pop(self):
        if self.top - 1 < -1:
            print("Stack is already empty...")
            return
        self.stack.pop()
        self.top = self.top - 1

    def peek(self):
        return self.stack[self.top]

    def printStack(self):
        print("\n")
        for i in self.stack:
            print(i)

st = Stack(5)
st.push(123)
st.push(245)
st.push(11)
st.push(23)
st.push(-5)
st.printStack()
st.push(-5)

lastInserted = st.peek()
print("Last Data is... ")
