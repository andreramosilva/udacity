import sys
import models as md

class MinHeap:
    def __init__(self,maxsize,val0):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize+1)
        self.Heap[0] = val0 #-1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2*pos)+1

    def is_leaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            if (self.Heap[pos].frequency > self.Heap[self.left_child(pos)].frequency) or self.Heap[pos].frequency > self.Heap[self.right_child(pos)].frequency:
                if self.Heap[self.left_child(pos)].frequency < self.Heap[self.right_child(pos)].frequency:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                else:
                    self.swap(pos,self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    def insert(self,element):
        if self.size >= self.maxsize:
            return
        self.size+=1
        self.Heap[self.size]=element

        current = self.size

        while self.Heap[current].frequency < self.Heap[self.parent(current)].frequency:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print_heap(self):
        for i in range(1, (self.size//2)+1):
            print(i, 2 * i, 2 * i + 1)
            print("Parent: " + str(self.Heap[i].value) + " " + str(self.Heap[i].frequency)+" Left child: " +
                  str(self.Heap[2 * i].value) + " " + str(self.Heap[2 * i].frequency)+" right child: " +
                  str(self.Heap[2 * i + 1].value) +
                  " " + str(self.Heap[2 * i + 1].frequency))

    def min_heap(self):
        for pos in range(self.size // 2, 0, -1):
            self.min_heapify(pos)

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.min_heapify(self.FRONT)
        return popped

def test_MinHeap():
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.min_heap()
    minHeap.print_heap()
    print("The Min val is " + str(minHeap.remove()))


def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

def frequency_char_in_string(string):
    frequency = {}
    for char in string:
        frequency[char]=string.count(char)

    return frequency

def add_tree_nodes_to_heap(frequency_dic):
    print(frequency_dic)
    nodes_heap = MinHeap(len(frequency_dic)-1, md.TreeNode(" ", frequency_dic[" "]))


    for index in frequency_dic:

        node = md.TreeNode(index, frequency_dic[index])

        nodes_heap.insert(node)

    #nodes_heap.print_heap()
    print(nodes_heap.min_heap())




if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    add_tree_nodes_to_heap(frequency_char_in_string(a_great_sentence))
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

   # encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))