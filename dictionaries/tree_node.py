import random


class TreeNode:
    def __init__(self, key=None, value=None, parent=None,
                 left=None, right=None):
        self.key = key
        self.parent = parent
        self.priority = random.randint(0, int(1e18))
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

    def update_value(self, value):
        self.value = value

    def set_parent(self, key, value):
        self.parent = self.__init__(key, value)

    def clone(self):
        return self.__init__(self.key, self.value, self.parent,
                             self.left, self.right)

    def __str__(self):
        return 'key = {} value = {}'.format(self.key, self.value)

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value
