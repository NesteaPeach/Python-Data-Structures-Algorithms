

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """
        :param value:
        :return: create new node
        """
        pass

    def prepend(self, value):
        """
        :param value:
        :return:  create new node and add it to the beginning
        """
        pass

    def insert(self, index, value):
        """
        :param index:
        :param value:
        :return: create new node, and insert in index
        """
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
