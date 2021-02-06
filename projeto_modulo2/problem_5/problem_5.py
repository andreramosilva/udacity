import hashlib
from _datetime import datetime




class Block:

    def __init__(self, timestamp, data, prev, prev_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = prev_hash
        self.prev = prev
        self.hash = self.calc_hash(timestamp, data )

    def calc_hash(self, time, data):
        string_toencode = str(time)+str(data)
        sha = hashlib.sha256()
        hash_str = string_toencode.encode('utf-8')
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
            self.tail = Block(timestamp, data, prev,prev.previous_hash)
        else:
            self.head = Block(timestamp, data, 0,0)
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
            current_block = current_block.prev
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
# Timestamp:  2021-02-06 16:55:08.979261
# data:  7
# SHA256 Hash:  fc0cfeabad3d5e784087c5f2ba2c537d1844da0e117604a62a3165183f587a90
# Prev Hash:  0
# Index:  1
# Timestamp:  2021-02-06 16:55:08.979255
# data:  6
# SHA256 Hash:  6c7a92b229674a471c07f0ae30a4973f22feb4c3e66abfdb34524e2690cf91c8
# Prev Hash:  0
# Index:  2
# Timestamp:  2021-02-06 16:55:08.979249
# data:  5
# SHA256 Hash:  047cd00af24967853115bdb2ce881a2e6df74c52a8e61acbc33e5fb08b6c3c0a
# Prev Hash:  0
# Index:  3
# Timestamp:  2021-02-06 16:55:08.979244
# data:  4
# SHA256 Hash:  f150314c2d377aa07b52e2b134aeb10fcce777914ae1574ff20ecaa5eaec673d
# Prev Hash:  0
# Index:  4
# Timestamp:  2021-02-06 16:55:08.979237
# data:  3
# SHA256 Hash:  abfb80a670d3535b1bf965bc23f43d7046d7eef9fbfeb6440a73d6b4bbf42c35
# Prev Hash:  0
# Index:  5
# Timestamp:  2021-02-06 16:55:08.979230
# data:  2
# SHA256 Hash:  080978d5f29dd7371d06b15ba97bbb683205b830e03775775bb80f80e4ac7701
# Prev Hash:  0
# Index:  6
# Timestamp:  2021-02-06 16:55:08.979220
# data:  arbitrary
# SHA256 Hash:  3ac086bacac7af238db3f4f3a51eb8cdd8aa715932323daa3ed3d80a4bf6009f
# Prev Hash:  0
# Index:  7
# Timestamp:  2021-02-06 16:55:08.979172
# data:  Genesis
# SHA256 Hash:  f5dde666020d473e777479dc36b7dd1b3c7dce938921bf694e9527c470385d11
# Prev Hash:  0






