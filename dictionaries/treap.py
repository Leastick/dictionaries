from dictionaries import simple_bst, tree_node


class Treap(simple_bst.SimpleBinarySearchingTree):

    def __init__(self):
        super().__init__()

    def __merge(self, left, right):
        if right is None:
            return left
        if left is None:
            return right
        if left.priority > right.priority:
            left.right = self.__merge(left.right, right)
            return left
        else:
            right.left = self.__merge(left, right.left)
            return right

    def __split(self, node, key):
        if node is None:
            return None, None
        else:
            if key > node.key:
                t1, t2 = self.__split(node.right, key)
                node.right = t1
                return node, t2
            else:
                t1, t2 = self.__split(node.left, key)
                node.left = t2
                return t1, node

    def __find_occurrence(self, node, key):
        t1, t2 = self.__split(self.root, key)
        x, t2 = self.__split(t2, key + 1)
        self.root = self.__merge(t1, self.__merge(x, t2))
        return x

    def contains_key(self, key):
        return self.__find_occurrence(self.root, key) is not None

    def insert(self, key, value):
        if self.contains_key(key):
            raise KeyError
        self.node_amount += 1
        node = tree_node.TreeNode(key, value)
        left, right = self.__split(self.root, key)
        self.root = self.__merge(self.__merge(left, node), right)

    def erase(self, key):
        self.node_amount -= 1
        t1, t2 = self.__split(self.root, key)
        x, t2 = self.__split(t2, key + 1)
        if x is None or x.key != key:
            raise KeyError
        self.root = self.__merge(t1, t2)



