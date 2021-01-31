class TreeNode:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.right = None
        self.left = None

    def get_val(self):
        return self.value

    def set_val(self, value):
        self.value = value

    def set_left_child(self, value):
        self.left = value

    def set_right_child(self, value):
        self.right = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        if self.left:
            return True
        else:
            return False

    def has_right_child(self):
        return self.right != None


class HuffmanTree:
    def __init__(self, value=None):
        self.root = TreeNode(value)

