import sys

from dictionaries.tree_node import TreeNode

sys.setrecursionlimit(1000 * 1000 * 1000)


class SimpleBinarySearchingTree:

    def __init__(self):
        self.root = None
        self.node_amount = 0

    def insert(self, key, value):
        for_insert = TreeNode(key, value)
        if self.contains_key(key):
            return
        self.node_amount += 1
        if self.root is None:
            subtree_root = None
            self.root = for_insert
        else:
            subtree_root = self.root
        while subtree_root is not None:
            if subtree_root.key <= for_insert.key:
                if subtree_root.right is not None:
                    subtree_root = subtree_root.right
                else:
                    subtree_root.right = for_insert
                    break
            else:
                if subtree_root.left is not None:
                    subtree_root = subtree_root.left
                else:
                    subtree_root.left = for_insert
                    break

    def __find_occurrence(self, node, key):
        if node is None or key == node.key:
            return node
        if key < node.key:
            return self.__find_occurrence(node.left, key)
        else:
            return self.__find_occurrence(node.right, key)

    def get(self, key):
        node = self.__find_occurrence(self.root, key)
        if node is None:
            raise KeyError
        return node.value

    def contains_key(self, key):
        return self.__find_occurrence(self.root, key) is not None

    def set(self, key, value):
        node = self.__find_occurrence(self.root, key)
        if node is None:
            raise KeyError
        node.value = value

    @staticmethod
    def __get_minimal(node):
        while node.left is not None:
            node = node.left
        return node

    def __erase(self, node, key):
        if node is None:
            raise KeyError
        if key < node.key:
            node.left = self.__erase(node.left, key)
        elif key > node.key:
            node.right = self.__erase(node.right, key)
        elif node.left is not None and node.right is not None:
            minimal = SimpleBinarySearchingTree.__get_minimal(node.right)
            node.key = minimal.key
            node.value = minimal.value
            node.right = self.__erase(node.right, node.key)
        else:
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node

    def erase(self, key):
        try:
            self.root = self.__erase(self.root, key)
        except KeyError:
            raise KeyError
        else:
            self.node_amount -= 1

    def __len__(self):
        return self.node_amount
