class Stack:

    MAX_SIZE = 3

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        if self.size() < Stack.MAX_SIZE:
            self.items.append(item)
        else:
            raise RuntimeError('Stack is full')

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items.pop()

    def display(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items)-1]


if __name__ == "__main__":
    st = Stack()

    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Size")
        print("5.Display")
        print("6.Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            if len(st.items) < Stack.MAX_SIZE:
                x = int(input("Enter the element to be pushed : "))
                st.push(x)
            else:
                print("Stack is full")
        elif choice == 2:
            x = st.pop()
            print("Popped element is : ", x)
        elif choice == 3:
            print("Element at the top is : ", st.peek())
        elif choice == 4:
            print("Size of stack ", st.size())
        elif choice == 5:
            st.display()
        elif choice == 6:
            break;
        else:
            print("Wrong choice")
        print()