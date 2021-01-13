import sys
from queue import PriorityQueue


class Node:
    def __init__(self, is_leaf: bool = False, left=None, right=None, count=0, char=None):
        self.is_leaf = is_leaf
        self.left = left
        self.right = right
        self.count = count
        self.char = char


class Tree:
    def __init__(self):
        self.head: Node = None

    def initialized(self) -> bool:
        return self.head is None


def huffman_encoding(data) -> Tree:
    if not data:
        raise Exception("data is not valid")

    # frequencies
    freq_map = {}

    for element in data:
        if element in freq_map.keys():
            freq_map[element] = freq_map[element] + 1
        else:
            freq_map[element] = 1

    # priority queue
    priority_q = PriorityQueue()
    # print(priority_q.get())
    # fill the queue
    for key, value in freq_map.items():
        priority_q.put((value, key))

    tree = Tree()

    # while not priority_q.empty():
    #     left = priority_q.get()
    #     right = priority_q.get()
    #
    #     if not tree.initialized() is None:
    #         left_node = Node(True, count=left[0], char=left[1])
    #         right_node = Node(True, count=right[0], char=right[1])
    #         total_count = left_node.count + right_node.count
    #         head = Node(False, left_node, right_node, total_count)
    #         tree.head = head
    #     # elif priority_q.

    return tree


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)
    huffman_encoding(a_great_sentence)

    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))
