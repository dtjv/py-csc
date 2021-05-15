from typing import Union


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Union['Node', None] = None


class LinkedList:
    __head: Union[Node, None] = None

    def __len__(self) -> int:
        count = 0
        currNode = self.__head

        while currNode is not None:
            currNode = currNode.next
            count += 1

        return count

    def add(self, value: int) -> 'LinkedList':
        newNode = Node(value)

        if self.__head is None:
            self.__head = newNode
        else:
            currNode = self.__head

            while currNode.next is not None:
                currNode = currNode.next

            currNode.next = newNode

        return self

    def remove(self, value: int) -> 'LinkedList':
        currNode = self.__head

        if currNode is not None and currNode.value == value:
            self.__head = currNode.next
        else:
            while currNode is not None:
                nextNode = currNode.next

                if nextNode is not None and nextNode.value == value:
                    currNode.next = nextNode.next
                    break
                else:
                    currNode = currNode.next

        return self

    def reverse(self) -> 'LinkedList':
        def reverseR(node: Union[Node, None]) -> Union[Node, None]:
            if node is None or node.next is None:
                return node

            newHead = reverseR(node.next)
            node.next.next = node
            node.next = None
            return newHead

        self.__head = reverseR(self.__head)

        return self

    def get_value_at_index(self, index: int) -> Union[int, None]:
        currNode = self.__head
        currIndex = 0

        while currNode is not None:
            if currIndex == index:
                return currNode.value

            currNode = currNode.next
            currIndex += 1

        return None
