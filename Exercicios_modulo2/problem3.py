###
# Problem 3: Huffman Coding
###
import sys
# Constants for the Huffman Tree
LEFT_BIT = "0"
RIGHT_BIT = "1"
class MinHeap():
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.size = 0
    def insert(self, value):
        '''Inserts the provided value into the heap.'''
        # If array is at capacity, expand it before inserting new value
        if self.size == len(self.array):
            new_array = [None] * (2 * len(self.array))
            for i, elem in enumerate(self.array):
                new_array[i] = elem
            self.array = new_array
        # Add element at the leftmost open space
        index = self.size
        self.array[index] = value
        # Ensure the heap shape. If the inserted value is less than its predecessors, swap the values as needed.
        while (index > 0):
            parent_index = (index - 1) // 2
            if self.array[index] < self.array[parent_index]:
                # Swap the element and its parent
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                index = parent_index
            else:
                # Order is correct, so stop
                break
        self.size += 1
    def get_min(self):
        '''Returns the root (min) element of the heap without removing it.'''
        return self.array[0]
    def delete_min(self):
        '''Removes the root (min) element of the heap.'''
        if self.size == 0:
            return
        # Replace the root with the last element of the heap
        self.size -= 1
        self.array[0] = self.array[self.size]
        self.array[self.size] = None
        # Ensure the heap shape. If the root is greater than its successors, swap the values as needed.
        self._min_heapify(0)
    def pop_min(self):
        '''Removes and returns the root (min) element of the heap.'''
        min_elem = self.get_min()
        self.delete_min()
        return min_elem
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
class HuffmanNode():
    def __init__(self, value = None, frequency = 0):
        self.frequency = frequency
        self.value = value
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.frequency < other.frequency
    def __str__(self):
        return f"['{self.value}':{self.frequency}]"
def build_huffman_tree(data):
    """
    Build the Huffman tree for the provided data.
    :param data: Data to encode.
    :return: Root node of the Huffman tree.
    """
    # Step 1 : Count the frequency of each character
    frequency_table = {}
    for ch in data:
        frequency_table[ch] = frequency_table.get(ch, 0) + 1
    # Step 2: Create "priority queue" (e.g. min-heap)
    priority_queue = MinHeap()
    for ch, frequency in frequency_table.items():
        new_node = HuffmanNode(ch, frequency)
        priority_queue.insert(new_node)
    # Create the Huffman tree
    while priority_queue.size > 1:
        # Step 3: Pop-out the two nodes with the minimum frequency
        node1 = priority_queue.pop_min()
        node2 = priority_queue.pop_min()
        # Step 4: Create new node by "combining" the two prior nodes, and insert it into the priority queue
        new_node = HuffmanNode(None, (node1.frequency + node2.frequency))
        new_node.left = node1
        new_node.right = node2
        priority_queue.insert(new_node)
    # Return the only item in the priority queue.
    # Note: Use "get_min" instead of "pop_min" to avoid heapifying unnecessarily.
    return priority_queue.get_min()
def generate_code_table(table, node, code):
    """
    Helper method to generate the table for the Huffman code by traversing the Huffman tree recursively.
    :param table: Table with the Huffman code.
    :param node: Starting node (of the Huffman tree) for traversing downward.
    :param code: Partial Huffman code so far (from the root until the provided node).
    :return: Table with the Huffman code.
    """
    # If it is a leaf node, insert code into the table
    if not node.left and not node.right:
        table[node.value] = code
        return table
    # Traverse to its child nodes
    if node.left:
        generate_code_table(table, node.left, code + LEFT_BIT)
    if node.right:
        generate_code_table(table, node.right, code + RIGHT_BIT)
    return table
def huffman_encoding(data):
    """
    Encode the provided data using the Huffman Coding.
    :param data: Data to encode.
    :return: Encoded version of the provided data.
    """
    # If data is empty, return it back
    if data is None or len(data) == 0:
        return data, None
    ### Phase 1: Build the Huffman Tree
    tree = build_huffman_tree(data)
    ### Phase 2: Generate the encoded data ###
    # Traverse tree to generate table
    code_table = generate_code_table({}, tree, "")
    # Encode the data
    encoded_data = ""
    for ch in data:
        encoded_data += code_table[ch]
    return encoded_data, tree
def huffman_decoding(encoded_data, tree):
    """
    Decode the provided data using the provided Huffman tree.
    :param encoded_data: Encoded data to be decoded with the provided Huffmann tree.
    :param tree: Root of the Huffman tree used to encode the provided data.
    :return: Decoded version of the provided data.
    """
    if encoded_data is None:
        return None
    decoded_data = ""
    node = tree # Start at the root of the tree
    for bit in encoded_data:
        if bit == LEFT_BIT:
            node = node.left
        elif bit == RIGHT_BIT:
            node = node.right
        # If node is a leaf node, append its character to the decoded string
        if not node.left and not node.right:
            decoded_data += node.value
            node = tree # Go back to the root of the tree
    return decoded_data
def test_huffman(sentence):
    codes = {}
    print (f"Size of the data: {sys.getsizeof(sentence)}")
    print (f"Content of the data: '{sentence}'")
    encoded_data, tree = huffman_encoding(sentence)
    if encoded_data and len(encoded_data) > 0:
        print (f"Size of the encoded data: {sys.getsizeof(int(encoded_data, base=2))}")
        print (f"Content of the encoded data: '{encoded_data}'")
    else:
        print ("Data was not encoded")
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Size of the decoded data: {sys.getsizeof(decoded_data)}")
    print(f"Content of the encoded data: '{decoded_data}'")
    print()
if __name__ == "__main__":
    # Sample test case #1
    test_huffman("AAAAAAABBBCCCCCCCDDEEEEEE")
    # Expect: Data of size 74 is encoded to size 32.
    # Sample test case #2
    test_huffman("The bird is the word")
    # Expect: Data of size 69 is encoded to size 36.
    # Edge case: Empty string
    test_huffman("")
    # Expect: Empty string yields "Data was not encoded" and returns empty string.
    # (Note: Empty strings seem to have size 49).
    # Edge case: None
    test_huffman(None)
    # Expect: 'None' yields "Data was not encoded" and returns 'None'.
    # (Note: None seems to have size 49).
    # Test case: Longer sentence
    test_huffman("In general, a data compression algorithm reduces the amount of memory (bits) required to represent a "
                 "message (data)")
    # Expect: Data of size 164 is encoded to size 88.
    # Test case: Paragraph #1
    test_huffman("In general, a data compression algorithm reduces the amount of memory (bits) required to represent a "
                 "message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to "
                 "receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this "
                 "problem, you have to implement the logic for both encoding and decoding.")
    # Expect: Data of size 421 is encoded to size 232.
    # Test case: Paragraph #2
    test_huffman("Create a new node with a frequency equal to the sum of the two nodes picked in the above step. "
                 "This new node would become an internal node in the Huffman tree, and the two nodes would become the "
                 "children. The lower frequency node becomes a left child, and the higher frequency node becomes the "
                 "right child. Reinsert the newly created node back into the priority queue.")
    # Expect: Data of size 417 is encoded to size 232.