class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def print(self):
        node = self.head

        while node is not None:
            print(node.value, end =" ")
            node = node.next
        print()


def union(list_1: LinkedList, list_2: LinkedList) -> LinkedList:
    list = LinkedList()
    unique_values_1 = set()
    unique_values_2 = set()
    node = list_1.head

    while node is not None:
        unique_values_1.add(node.value)
        list.append(node.value)
        node = node.next

    node = list_2.head
    while node is not None:
        if node.value not in unique_values_1 and node.value not in unique_values_2:
            list.append(node.value)
            unique_values_2.add(node.value)
        node = node.next

    return list


def intersection(list_1, list_2) -> LinkedList:
    list = LinkedList()
    unique_values_1 = set()
    unique_values_2 = set()
    node = list_1.head

    while node is not None:
        unique_values_1.add(node.value)
        node = node.next

    node = list_2.head
    while node is not None:
        if node.value in unique_values_1 and node.value not in unique_values_2:
            list.append(node.value)
            unique_values_2.add(node.value)
        node = node.next

    return list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test 1")
print("List 1")
linked_list_1.print()
print("List 2")
linked_list_2.print()
print("Union result")
union(linked_list_1, linked_list_2).print()
print("Intersection result")
intersection(linked_list_1, linked_list_2).print()


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("\nTest 2")
print("List 3")
linked_list_3.print()
print("List 4")
linked_list_4.print()
print("Union result")
union(linked_list_3, linked_list_4).print()
print("Intersection result")
intersection(linked_list_3, linked_list_4).print()


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("Test 3")
print("List 5")
linked_list_5.print()
print("List 6")
linked_list_6.print()
print("Union result")
union(linked_list_5, linked_list_6).print()
print("Intersection result")
intersection(linked_list_5, linked_list_6).print()
