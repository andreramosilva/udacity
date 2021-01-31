import hashlib
from datetime import datetime




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

    def add_block(self,data):
        if self.head != None:
            prev = self.tail
            self.tail = Block(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),data,prev)
        else:
            self.head = Block(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),data,0)


print(new_block.timestamp,new_block.data,new_block.previous_hash,new_block.hash)