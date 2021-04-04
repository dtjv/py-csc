class Stack:
    def __init__(self):
        self.__private_store = []
        self.currentIdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentIdx == len(self.__private_store):
            raise StopIteration

        item = self.__private_store[self.currentIdx]
        self.currentIdx += 1

        return item

    def __len__(self):
        return len(self.__private_store)

    def push(self, item):
        self.__private_store = [item, *self.__private_store]

    def pop(self):
        item = self.__private_store[0]
        self.__private_store = self.__private_store[1:]
        return item

