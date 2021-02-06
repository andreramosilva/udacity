class LRU_Cache(object):

    def __init__(self, capacity):
        self.size = 5
        self.data = {}
        self.calls = []
        # Initialize class variables

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.calls:
            self.calls.remove(key)
            self.calls.append(key)
        return self.data.get(key, -1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.get(value) == -1:
            if self.size == 0:
                del self.data[self.calls[0]]
                self.calls.remove(self.calls[0])

                self.size += 1

            self.data[key] = value
            self.calls.append(key)
            self.size -= 1


#test cases :
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(8))  # returns -1 because 8 is not present in the cache

print(our_cache.get(2))  # returns 2

print(our_cache.data) # returns {1: 1, 2: 2, 4: 4, 5: 5, 6: 6}

#output final with all the tests
# (base) andreramossilva@MacBook-Pro projeto_modulo2 % python problem_1.py
# 1
# 2
# -1
# -1
# -1
# 2
# {1: 1, 2: 2, 4: 4, 5: 5, 6: 6}
