from src.ds.stack import Stack


class Queue:
    def __init__(self):
        self.__in_stack = Stack()
        self.__out_stack = Stack()

    def __len__(self):
        return len(self.__in_stack) + len(self.__out_stack)

    def enqueue(self, item):
        self.__in_stack.push(item)

    def dequeue(self):
        if len(self.__out_stack) == 0:
            while len(self.__in_stack) > 0:
                self.__out_stack.push(self.__in_stack.pop())

        return self.__out_stack.pop()
