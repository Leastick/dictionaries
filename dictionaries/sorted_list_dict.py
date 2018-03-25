from dictionaries import dict_item, list_dict


class SortedListDict(list_dict.ListDict):

    def __init__(self):
        super().__init__()
        self.list = []

    def insert(self, key, value):
        insertion_index = 0
        if self.contains_key(key):
            raise KeyError('Key already exist')
        for item in self.list:
            if item.get_key() > key:
                break
            insertion_index += 1
        self.list.insert(insertion_index, dict_item.DictItem(key, value))

    def __find_occurrence_index__(self, key):
        left = 0
        right = len(self.list)
        while right - left > 1:
            middle = (left + right) // 2
            if self.list[middle].get_key() > key:
                right = middle
            else:
                left = middle
        if right != 0 and self.list[left].get_key() == key:
            return left
        else:
            raise KeyError('Key not founded')

