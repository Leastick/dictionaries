class DictWrapper:
    def __init__(self):
        self._dict = {}

    def contains_key(self, key):
        return key in self._dict

    def insert(self, key, value):
        self._dict[key] = value

    def erase(self, key):
        self._dict.pop(key)