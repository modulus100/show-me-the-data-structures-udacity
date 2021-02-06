import sys
from queue import PriorityQueue, Queue
from typing import Tuple


class Node:
    def __init__(self, is_leaf: bool = False, left=None, right=None, freq=0, char=None):
        self.is_leaf = is_leaf
        self.left = left
        self.right = right
        self.freq = freq
        self.char = char

    def __gt__(self, other):
        return self.freq > other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __str__(self):
        char = self.char if self.char is not None else "+"
        return char\
            + ' freq: ' + str(self.freq)\
            + ' is leaf: ' + str(self.is_leaf)


class Tree:
    def __init__(self, head: Node = None):
        self.head: Node = head

    def _print_tree(self, node: Node, level: int):
        if node is not None:
            self._print_tree(node.left, level + 1)
            print(' ' * 4 * level + '->', node)
            self._print_tree(node.right, level + 1)

    def print_tree(self):
        self._print_tree(self.head, 0)


class HuffmanCoding:
    def encode(self, data: str) -> Tuple[str, Tree]:
        if not data:
            raise Exception("data is not valid")

        freq_map = self.count_frequencies(data)
        queue = PriorityQueue()

        # init nodes
        for key, value in freq_map.items():
            node = Node(freq=value, char=key)
            queue.put(node)

        tree = self.build_tree(queue)
        char_code_map = self.build_char_code_map(tree.head)
        encoded_data = self.build_encoded_data(data, char_code_map)
        return encoded_data, tree

    def build_char_code_map(self, head: Node) -> dict:
        char_code_map = {}
        self.preorder_traversal(head.left, char_code_map, "0")
        self.preorder_traversal(head.right, char_code_map, "1")
        return char_code_map

    def preorder_traversal(self, node: Node, char_code_map: dict, code: str):
        if node is None:
            return
        if node.char is not None:
            char_code_map[node.char] = code

        self.preorder_traversal(node.left, char_code_map, code + "0")
        self.preorder_traversal(node.right, char_code_map, code + "1")

    def build_encoded_data(self, data: str, char_code_map: dict) -> str:
        encoded_data = ""
        for element in data:
            encoded_data += char_code_map[element]
        return encoded_data

    def build_tree(self, queue) -> Tree:
        while not queue.empty():
            left_node: Node = queue.get()
            if queue.empty():
                return Tree(left_node)

            right_node: Node = queue.get()
            self.set_is_leaf(left_node)
            self.set_is_leaf(right_node)

            freq_sum = left_node.freq + right_node.freq
            parent_node = Node(False, left_node, right_node, freq_sum)
            queue.put(parent_node)

    def set_is_leaf(self, node: Node):
        if node.left is None and node.right is None:
            node.is_leaf = True
        else:
            node.is_leaf = False

    def count_frequencies(self, data: str):
        freq_map = {}
        for element in data:
            if element in freq_map.keys():
                freq_map[element] += 1
            else:
                freq_map[element] = 1
        return freq_map

    def decode(self, encoded_data: str, tree: Tree):
        if not encoded_data:
            raise Exception("data is not valid")
        decoded_data = ""

        while encoded_data != "":
            encoded_data, decoded_bits = self.decode_batch_of_bits(encoded_data, tree.head)
            decoded_data += decoded_bits

        return decoded_data

    def decode_batch_of_bits(self, encoded_data: str, node: Node) -> Tuple[str, str]:
        for index, element in enumerate(encoded_data):
            if node.char is not None:
                return encoded_data[index:], node.char
            elif element == "0":
                node = node.left
            elif element == "1":
                node = node.right

        if node.char is not None:
            return "", node.char

        raise Exception("encoded data is not valid")


if __name__ == "__main__":
    codes = {}
    huffman = HuffmanCoding()

    a_great_sentence = "The bird is the word"
    # a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman.encode(a_great_sentence)
    # tree.print_tree()

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.decode(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
