from dictionaries import dict_item


class ListDict:

    def __init__(self):
        self.list = []

    def insert(self, key, value):
        if self.contains_key(key):
            raise KeyError('Key already exist')
        self.list.append(dict_item.DictItem(key, value))

    def set(self, key, value):
        update_index = self.__find_occurrence_index__(key)
        self.list[update_index].update_value(value)

    def __find_occurrence_index__(self, key):
        index = 0
        for item in self.list:
            if item.get_key() == key:
                return index
            index += 1
        raise KeyError('Key not founded')

    def erase(self, key):
        occurrence_index = self.__find_occurrence_index__(key)
        self.list = self.list[: occurrence_index] + self.list[occurrence_index + 1:]

    def contains_key(self, key):
        try:
            occurrence_index = self.__find_occurrence_index__(key)
            return True
        except KeyError:
            return False

    def get(self, key):
        occurrence_index = self.__find_occurrence_index__(key)
        return self.list[occurrence_index].get_value()

    def __len__(self):
        return len(self.list)
