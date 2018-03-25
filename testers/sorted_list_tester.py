import copy
import time

from dictionaries import sorted_list_dict
from testers import tester


class SortedListTester(tester.Tester):
    def __init__(self, iter_amount, test_directory, result_directory):
        super().__init__(sorted_list_dict.SortedListDict, iter_amount,
                         test_directory, result_directory + '/sorted_list_dict',
                         'sorted_list_dict')
        self.MAX_ITERATIONS = 2000
        self.MEASURE_LABEL = [100, 200, 500, 1000, 1100, 1200, 1600, 1700, 1800, 1900, 2000]

    @staticmethod
    def erase_test(_dict, keys):
        keys.sort()
        first_copy = copy.deepcopy(_dict)
        second_copy = copy.deepcopy(_dict)
        measurement_started = time.time()
        first_copy.erase(keys[0])
        worst_time = time.time() - measurement_started
        measurement_started = time.time()
        second_copy.erase(keys[len(keys) - 1])
        best_time = time.time() - measurement_started
        return worst_time, best_time
