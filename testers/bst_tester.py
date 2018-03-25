import copy
import time

from dictionaries import simple_bst
from testers import tester


class BSTTester(tester.Tester):
    def __init__(self, iter_amount, test_directory, result_directory):
        super().__init__(simple_bst.SimpleBinarySearchingTree, iter_amount,
                         test_directory, result_directory + '/bst',
                         'bst')
        self.MAX_ITERATIONS = 10000
        self.MEASURE_LABEL = [100, 200, 500, 1000,
                              1100, 1200, 1600, 1700,
                              1800, 1900, 2000, 3500,
                              4000, 5000, 6000, 7000,
                              8000, 9600, 9700, 9800,
                              9900, 10_000]

    @staticmethod
    def erase_test(_dict, keys):
        keys.sort()
        first_copy = copy.deepcopy(_dict)
        second_copy = copy.deepcopy(_dict)
        measurement_started = time.time()
        first_copy.erase(keys[len(keys) - 1])
        worst_time = time.time() - measurement_started
        measurement_started = time.time()
        second_copy.erase(keys[0])
        best_time = time.time() - measurement_started
        return worst_time, best_time
