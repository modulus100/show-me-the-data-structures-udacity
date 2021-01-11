import sys
from queue import PriorityQueue


class Node:

    def __init__(self, is_leaf: bool = False, left=None, right=None, count=0, char=None):
        self.is_leaf = is_leaf
        self.left = left
        self.right = right
        self.count = count
        self.char = char


def huffman_encoding(data):
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

    for key, value in freq_map.items():
        priority_q.put((value, key))

    while not priority_q.empty():
        print(priority_q.get())


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
