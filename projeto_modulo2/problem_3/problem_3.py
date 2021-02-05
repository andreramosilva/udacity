import sys
#import models as md

LEFT_BIT = "0"
RIGHT_BIT = "1"

class MinHeap:
    def __init__(self, capacity = 10):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, value):

        if self.size == len(self.array):
            new_array = [None] *(2*len(self.array))
            for i, element in enumerate(self.array):
                new_array[i] = element
            self.array = new_array

        index = self.size
        self.array[index] = value

        while (index > 0):
            parent_index = (index - 1) // 2
            if self.array[index] < self.array[parent_index]:
                self.array[index],self.array[parent_index] = self.array[parent_index], self.array[index]
                index = parent_index
            else:
                break
        self.size += 1

    def get_min(self):
        return self.array[0]

    def delete_min(self):
        if self.size == 0:
            return

        self.size -= 1
        self.array[0] = self.array[self.size]
        self.array[self.size] = None

        self._min_heapify(0)

    def pop_min(self):
        min_el = self.get_min()
        self.delete_min()
        return min_el

    def _min_heapify(self, index):
        left = (2 * index) + 1
        right = (2 * index) + 2
        smallest = index

        if left < self.size and self.array[left] < self.array[smallest]:
            smallest = left
        if right < self.size and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != index:
            self.array[index], self.array[smallest] = self.array[smallest], self.array[index]
            self._min_heapify(smallest)

class HuffmanNode:
    def __init__(self, value = None , frequency = 0):
        self.frequency = frequency
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __str__(self):
        return f"['{self.value}': {self.frequency}]"


def build_huffman_tree(data):
    '''
    Build the huffman tree for data
    :param data: string data to encode
    :return: root node of a huffman tree
    '''
    frequency_table = {}
    for ch in data:
        frequency_table[ch] = frequency_table.get(ch , 0) + 1

    priority_queue = MinHeap()
    for ch , frequency in frequency_table.items():
        new_node = HuffmanNode(ch,frequency)
        priority_queue.insert(new_node)

    while priority_queue.size > 1:
        node1 = priority_queue.pop_min()
        node2 = priority_queue.pop_min()

        new_node = HuffmanNode(None,(node1.frequency + node2.frequency))
        new_node.left = node1
        new_node.right = node2
        priority_queue.insert(new_node)

    return priority_queue.get_min()

def generate_code_table(table,node,code):
    if not node.left and not node.right:
        table[node.value] = code
        return table
    if node.left:
        generate_code_table(table,node.left,code + LEFT_BIT)
    if node.right:
        generate_code_table(table, node.right , code + RIGHT_BIT)
    return table


def huffman_encoding(data):
    if data is None or len(data) == 0:
        return data, None

    tree = build_huffman_tree(data)

    code_table = generate_code_table({},tree,"")
    encoded_data = ""
    for ch in data:
        encoded_data += code_table[ch]
    return encoded_data,tree


def huffman_decoding(data, tree):
    if data is None:
        return None
    decoded_data = ""
    node = tree
    for bit in data:
        if bit == LEFT_BIT:
            node = node.left
        elif bit == RIGHT_BIT:
            node = node.right
        if not node.left and not node.right:
            decoded_data += node.value
            node = tree
    return decoded_data





if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    encode = huffman_encoding(a_great_sentence)
    print(encode)
    decode = huffman_decoding(encode,encode[1])
    print(decode)

    a_great_sentence = "The bird is not the word"
    encode = huffman_encoding(a_great_sentence)
    print(encode)
    decode = huffman_decoding(encode,encode[1])
    print(decode)


    a_great_sentence = "The buddy is the world"
    encode = huffman_encoding(a_great_sentence)
    print(encode)
    decode = huffman_decoding(encode,encode[1])
    print(decode)

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

   # encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))
