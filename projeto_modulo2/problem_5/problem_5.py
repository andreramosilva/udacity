import hashlib
from _datetime import datetime




class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        now = datetime.today()

        timestamp = datetime.timestamp(now)

        if self.head != None:
            prev = self.tail
            self.tail = Block(timestamp, data, prev)
        else:
            self.head = Block(timestamp, data, 0)
            self.tail = self.head

    def print_block_chain(self):
        current_block = self.tail
        index = 0
        while current_block:
            print("Index: ", index)
            print("Timestamp: ", datetime.fromtimestamp(current_block.timestamp))
            print("data: ", current_block.data)
            print("SHA256 Hash: ", current_block.hash)
            print("Prev Hash: ", current_block.previous_hash)
            current_block = current_block.previous_hash
            index += 1

# test case 1 :
new_block = BlockChain()
new_block.add_block("Genesis")
new_block.add_block("arbitrary")
new_block.add_block("2")
new_block.add_block("3")
new_block.add_block("4")
new_block.add_block("5")
new_block.add_block("6")
new_block.add_block("7")

new_block.print_block_chain()

#Example output:
# Index:  0
# Timestamp:  2021-02-05 09:42:36.457762
# data:  7
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  <__main__.Block object at 0x7f949a51f310>
# Index:  1
# Timestamp:  2021-02-05 09:42:36.457757
# data:  6
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  <__main__.Block object at 0x7f949a51f2b0>
# Index:  2
# Timestamp:  2021-02-05 09:42:36.457752
# data:  5
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  <__main__.Block object at 0x7f949a51f250>
# Index:  3
# Timestamp:  2021-02-05 09:42:36.457747
# data:  4
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  <__main__.Block object at 0x7f949a51f1f0>
# Index:  4
# Timestamp:  2021-02-05 09:42:36.457742
# data:  3
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  <__main__.Block object at 0x7f949a51f190>
# Index:  5
# Timestamp:  2021-02-05 09:42:36.457737
# data:  2
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  <__main__.Block object at 0x7f949a4cc310>
# Index:  6
# Timestamp:  2021-02-05 09:42:36.457729
# data:  arbitrary
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  <__main__.Block object at 0x7f949a4a0130>
# Index:  7
# Timestamp:  2021-02-05 09:42:36.457687
# data:  Genesis
# SHA256 Hash:  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
# Prev Hash:  0






