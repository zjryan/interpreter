class EmptyStackError(Exception):
    pass


class Stack(object):
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def pop(self):
        if len(self.array) > 0:
            del self.array[-1]
        else:
            raise EmptyStackError("the stack now is empty")

    def top(self):
        if len(self.array) > 0:
            return self.array[-1]
        else:
            raise EmptyStackError("the stack now is empty")

    def is_empty(self):
        return len(self.array) == 0

    def len(self):
        return len(self.array)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()