import sys
from queue import PriorityQueue


class Node:
    def __init__(self, is_leaf: bool = False, left=None, right=None, freq=0, char=None):
        self.is_leaf = is_leaf
        self.left = left
        self.right = right
        self.freq = freq
        self.char = char

    def __gt__(self, other):
        return self.freq > other.count

    def __eq__(self, other):
        return self.freq == other.count

    def __str__(self):
        return 'is leaf: ' + str(self.is_leaf)\
               + ' count: ' + str(self.freq)\
               + ' char: ' + str(self.char)


class Tree:
    def __init__(self, head: Node = None):
        self.head: Node = head

    def _print_tree(self, node: Node, level: int):
        if node is not None:
            self._print_tree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.char, ' count: ', node.freq, ' is leaf: ', node.is_leaf)
            self._print_tree(node.right, level + 1)

    def print_tree(self):
        self._print_tree(self.head, 0)


def huffman_encoding(data) -> Tree:
    if not data:
        raise Exception("data is not valid")

    # frequencies
    freq_map = {}

    for element in data:
        if element in freq_map.keys():
            freq_map[element] += 1
        else:
            freq_map[element] = 1

    # priority queue
    queue = PriorityQueue()

    for key, value in freq_map.items():
        node = Node(freq=value, char=key)
        queue.put(node)

    while not queue.empty():
        node1: Node = queue.get()
        if queue.empty():
            return Tree(node1)

        node2: Node = queue.get()
        set_is_leaf(node1)
        set_is_leaf(node2)
        parent_node = Node(False, node1, node2, node1.freq + node2.freq)
        queue.put(parent_node)


def set_is_leaf(node: Node):
    if node.left is None and node.right is None:
        node.is_leaf = True
    else:
        node.is_leaf = False


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)
    tree = huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")
    tree.print_tree()

    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))
