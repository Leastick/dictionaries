class DictItem:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

    def update_value(self, value):
        self.value = value

    def __str__(self):
        return 'key = {} value = {}'.format(self.key, self.value)

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value
