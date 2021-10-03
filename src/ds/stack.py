class Stack:
    def __init__(self):
        self.__store = []
        self.currentIdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentIdx == len(self.__store):
            raise StopIteration

        item = self.__store[self.currentIdx]
        self.currentIdx += 1

        return item

    def __len__(self):
        return len(self.__store)

    def push(self, item):
        self.__store = [item, *self.__store]

    def pop(self):
        if len(self.__store) == 0:
            return None

        item, self.__store = [self.__store[0], self.__store[1:]]
        return item
