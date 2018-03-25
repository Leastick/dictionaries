import random
import unittest

from dictionaries import dict_item, hashtable, list_dict, treap, sorted_list_dict, primes
from dictionaries.simple_bst import SimpleBinarySearchingTree
from dictionaries.tree_node import TreeNode

random.seed()


class TestListDictionary(unittest.TestCase):

    @staticmethod
    def init_dict():
        dictionary = list_dict.ListDict()
        return dictionary

    def test_insert(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        result_list = [dict_item.DictItem(1, 2), dict_item.DictItem(2, 3)]
        self.assertEquals(dictionary.list, result_list)

    def test_erase_erased_element_should_be_erased(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        dictionary.insert(3, 4)
        dictionary.erase(2)
        result_list = [dict_item.DictItem(1, 2), dict_item.DictItem(3, 4)]
        self.assertEquals(dictionary.list, result_list)

    def test_len_dict_with_three_elements_has_len_three(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        dictionary.insert(3, 4)
        result_list = [dict_item.DictItem(1, 2), dict_item.DictItem(2, 3),
                       dict_item.DictItem(3, 4)]
        self.assertEquals(len(dictionary), len(result_list))

    def test_contains_key_exist(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        self.assertTrue(dictionary.contains_key(1))

    def test_contains_key_does_not_exist(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        self.assertFalse(dictionary.contains_key(3))

    def test_get_returned_expected_value(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        self.assertEquals(dictionary.get(1), 2)

    def test_set_should_raise_key_error_when_key_not_founded(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        self.assertRaises(KeyError, dictionary.set, 4, 6)

    def test_set_should_update_value(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        dictionary.set(2, 4)
        result_list = [dict_item.DictItem(1, 2), dict_item.DictItem(2, 4)]
        self.assertEquals(dictionary.list, result_list)

    def test_insert_should_raise_keyerror(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        self.assertRaises(KeyError, dictionary.insert, 1, 2)

    def test_find_occurrence_index_should_raise_keyerror(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        self.assertRaises(KeyError, dictionary.__find_occurrence_index__, 100500)

    def test_big_input(self):
        dictionary = self.init_dict()
        dictionary.insert(1, 2)
        dictionary.insert(2, 3)
        for i in range(3, 1000):
            dictionary.insert(i, i)
        all_founded = True
        for i in range(1, 1000):
            if not dictionary.contains_key(i):
                all_founded = False
                break
        self.assertTrue(all_founded)


class TestSortedListDictionary(TestListDictionary):

    @staticmethod
    def init_dict():
        dictionary = sorted_list_dict.SortedListDict()
        return dictionary

    def test_sorted_dict_should_be_sorted(self):
        dictionary = TestSortedListDictionary.init_dict()
        list_of_keys = []
        for item in dictionary.list:
            list_of_keys.append(item.get_key())
        for i in range(1, len(list_of_keys)):
            self.assertTrue(list_of_keys[i] < list_of_keys[i - 1])


class TestHashTable(unittest.TestCase):
    @staticmethod
    def init_dict():
        dictionary = hashtable.HashTable()
        dictionary.insert(2, 3)
        dictionary.insert(1, 2)
        return dictionary

    def test_get_bucket(self):
        dictionary = self.init_dict()
        self.assertEquals(dictionary.__get_bucket__(2), 2)

    def test_get_bucket_large(self):
        dictionary = self.init_dict()
        self.assertEquals(dictionary.__get_bucket__(12345),
                          12345 % len(dictionary.list))

    def test_insert(self):
        dictionary = self.init_dict()
        dictionary.insert(3, 4)
        all_keys_founded = True
        if not dictionary.list[dictionary.__get_bucket__(1)].contains_key(1):
            all_keys_founded = False
        if not dictionary.list[dictionary.__get_bucket__(2)].contains_key(2):
            all_keys_founded = False
        if not dictionary.list[dictionary.__get_bucket__(3)].contains_key(3):
            all_keys_founded = False
        self.assertTrue(all_keys_founded)

    def test_contains_key_exist(self):
        dictionary = self.init_dict()
        dictionary.insert(100500, 1)
        self.assertTrue(dictionary.list[dictionary.__get_bucket__(100500)].
                        contains_key(100500))

    def test_contains_key_does_not_exist(self):
        dictionary = self.init_dict()
        dictionary.insert(100500, 1)
        self.assertFalse(dictionary.list[dictionary.__get_bucket__(100501)].
                         contains_key(100501))

    def test_len(self):
        dictionary = self.init_dict()
        for i in range(3, 10):
            dictionary.insert(i, i)
        self.assertEquals(len(dictionary), 9)

    def test_get(self):
        dictionary = self.init_dict()
        self.assertEquals(dictionary.get(1), 2)

    def test_set(self):
        dictionary = self.init_dict()
        dictionary.set(2, 1000)
        self.assertEquals(dictionary.get(2), 1000)

    def test_extend(self):
        dictionary = hashtable.HashTable()
        for i in range(0, 1000):
            dictionary.insert(i, i)
        all_founded = True
        for i in range(0, 1000):
            if not dictionary.contains_key(i):
                all_founded = False
                break
        self.assertTrue(all_founded)


class TestPrimes(unittest.TestCase):
    def test_modulo_binary_exp_1(self):
        self.assertEqual(primes.modulo_binary_exp(1234, 56, 19), 1)

    def test_modulo_binary_exp_2(self):
        self.assertEqual(primes.modulo_binary_exp(1000000009, 89, 117), 73)

    def test_fermat_probabiliy_test_check_prime(self):
        self.assertTrue(primes.fermat_primality_test(100000007))

    def test_fermat_probability_test_check_not_prime(self):
        self.assertFalse(primes.fermat_primality_test(100000005))

    def test_fermat_probability_test_check_carmichael_number(self):
        self.assertTrue(primes.fermat_primality_test(561))

    def test_gcd_1(self):
        self.assertEqual(primes.gcd(2 * 3 * 17 * 41 * 2 * 2, 17), 17)

    def test_gcd_2(self):
        self.assertEqual(primes.gcd(2 * 3 * 17 * 41 * 2 * 2, 19), 1)

    def test_get_next_prime_1(self):
        self.assertEqual(primes.get_next_prime(2), 3)

    def test_get_next_prime_2(self):
        self.assertEqual(primes.get_next_prime(39), 41)

    def test_get_next_prime_3(self):
        self.assertEqual(primes.get_next_prime(560), 561)
        "561 - число Кармайкла, поэтому тест Ферма  \
        принимает его за простое число"


# Константы для настройки количества элементов, добавляемых в словарь и количество раз, которые мы прогоняем тесты
# Для BST и Treap
REPEATS = 10
N = 1000
MAX_RANDOM = 1e18


class TestBST(unittest.TestCase):
    @staticmethod
    def __init_bst():
        bst = SimpleBinarySearchingTree()
        return bst

    @staticmethod
    def __dfs(v, node):
        if v is None:
            return False
        if v == node:
            return True
        return TestBST.__dfs(v.left, node) or TestBST.__dfs(v.right, node)

    @staticmethod
    def generate_keys(n, forbidden_keys=[]):
        keys = []
        for j in range(n):
            x = random.randint(0, MAX_RANDOM)
            while x in keys or x in forbidden_keys:
                x = random.randint(0, MAX_RANDOM)
            keys.append(x)
        return keys

    def test_insert(self):
        for i in range(0, REPEATS):
            bst = self.__init_bst()
            keys = self.generate_keys(N)
            values = [random.randint(0, MAX_RANDOM) for _ in range(N)]
            random.shuffle(values)
            for j in range(N):
                bst.insert(keys[j], values[j])
            for j in range(N):
                self.assertTrue(TestBST.__dfs(bst.root, TreeNode(
                    keys[j],
                    values[j])))

    def test_contains_key(self):
        for i in range(REPEATS):
            bst = self.__init_bst()
            keys = self.generate_keys(N)
            values = [random.randint(0, MAX_RANDOM) for _ in range(N)]
            for j in range(N):
                bst.insert(keys[j], values[j])
            for j in range(N):
                self.assertTrue(bst.contains_key(keys[j]))
            not_in_tree = self.generate_keys(N, keys)
            for j in range(N):
                self.assertFalse(bst.contains_key(not_in_tree[j]))

    def test_erase(self):
        for i in range(REPEATS):
            bst = self.__init_bst()
            keys = self.generate_keys(N)
            values = [random.randint(0, MAX_RANDOM) for _ in range(N)]
            for j in range(N):
                bst.insert(keys[j], values[j])
            additional_keys = self.generate_keys(N, keys)
            additional_values = [random.randint(0, MAX_RANDOM) for _ in range(N)]
            for j in range(N):
                bst.insert(additional_keys[j], additional_values[j])
            for j in range(N):
                bst.erase(keys[j])
            for j in range(N):
                self.assertFalse(self.__dfs(bst.root, TreeNode(keys[j],
                                                               values[j])))
            for j in range(N):
                self.assertTrue(self.__dfs(bst.root, TreeNode(additional_keys[j],
                                                              additional_values[j])))

    def test_get(self):
        for i in range(REPEATS):
            bst = self.__init_bst()
            keys = self.generate_keys(N)
            dictionary = dict()
            values = [random.randint(0, MAX_RANDOM) for _ in range(N)]
            for j in range(N):
                dictionary[keys[j]] = values[j]
                bst.insert(keys[j], values[j])
            for j in range(N):
                self.assertEqual(dictionary[keys[j]], bst.get(keys[j]))
            not_in_tree = self.generate_keys(N, keys)
            for j in range(N):
                self.assertRaises(KeyError, bst.get, not_in_tree[j])

    def test_set(self):
        for i in range(REPEATS):
            bst = self.__init_bst()
            keys = self.generate_keys(N)
            values = [random.randint(0, MAX_RANDOM) for _ in range(N)]
            not_in_tree = self.generate_keys(N, keys)
            for j in range(N):
                bst.insert(keys[j], not_in_tree[j])
            for j in range(N):
                x = random.randint(MAX_RANDOM * 10, MAX_RANDOM * 100)
                bst.set(keys[j], x)
                self.assertTrue(self.__dfs(bst.root, TreeNode(keys[j], x)))
                self.assertFalse(self.__dfs(bst.root, TreeNode(keys[j], values[j])))
            for j in range(N):
                self.assertRaises(KeyError, bst.set, not_in_tree[j], random.randint(0, MAX_RANDOM))

    def test_len(self):
        for i in range(REPEATS):
            bst = self.__init_bst()
            keys = self.generate_keys(N)
            values = [random.randint(0, MAX_RANDOM) for _ in range(N)]
            for j in range(N):
                bst.insert(keys[j], values[j])
                self.assertEqual(len(bst), j + 1)
            n = random.randint(0, N)
            for j in range(n):
                bst.erase(keys[j])
                self.assertEqual(len(bst), N - j - 1)


class TestTreap(TestBST):
    @staticmethod
    def __init_bst():
        dictionary = treap.Treap()
        return dictionary

if __name__ == '__main__':
    unittest.main()
