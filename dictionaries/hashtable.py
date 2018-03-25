from dictionaries import dict_item, list_dict, primes


class HashTableItem(dict_item.DictItem):

    def __init__(self, key=None, value=None, key_name=None):
        super().__init__(key, value)
        self.key_name = key_name

    def get_key_name(self):
        return self.key_name


class HashTableList(list_dict.ListDict):

    def __init__(self, hash_func=hash):
        super().__init__()
        self.hash_func = hash_func

    def insert(self, key, value):
        hash_key = self.hash_func(key)
        if self.contains_key(hash_key):
            raise KeyError('Key already exist')
        self.list.append(HashTableItem(hash_key, value, key))

    def __find_occurrence_index__(self, key):
        index = 0
        hash_key = self.hash_func(key)
        for item in self.list:
            if item.get_key() == hash_key and item.get_key_name() == key:
                return index
            index += 1
        raise KeyError('Key not founded')


class HashTable:

    def __init__(self, hash_func=hash):
        self.MAGIC_CONSTANT = 5
        self.size = 23
        self.elements_counter = 0
        self.list = []
        self.hash_func = hash_func
        for i in range(0, self.size):
            self.list.append(HashTableList())

    def __get_bucket__(self, key):
        return self.hash_func(key) % self.size

    def insert(self, key, value):
        bucket = self.__get_bucket__(key)
        self.list[bucket].insert(key, value)
        self.elements_counter += 1
        if self.elements_counter > self.MAGIC_CONSTANT * self.size:
            self.__extend__()

    def erase(self, key):
        bucket = self.__get_bucket__(key)
        self.list[bucket].erase(key)
        self.elements_counter -= 1

    def contains_key(self, key):
        bucket = self.__get_bucket__(key)
        return self.list[bucket].contains_key(key)

    def set(self, key, value):
        bucket = self.__get_bucket__(key)
        self.list[bucket].set(key, value)

    def get(self, key):
        bucket = self.__get_bucket__(key)
        return self.list[bucket].get(key)

    def __extend__(self):
        data = []
        for bucket in self.list:
            for item in bucket.list:
                data.append(item)
        self.list = []
        self.size = primes.get_next_prime(2 * self.size)
        for i in range(0, self.size):
            self.list.append(list_dict.ListDict())
        for item in data:
            self.insert(item.get_key(), item.get_value())

    def __len__(self):
        return self.elements_counter
