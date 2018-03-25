import copy
import time

from dictionaries import list_dict
from testers import tester


class ListTester(tester.Tester):
    def __init__(self, iter_amount, test_directory, result_directory):
        super().__init__(list_dict.ListDict, iter_amount,
                         test_directory, result_directory + '/list_dict',
                         'list_dict')
        self.MAX_ITERATIONS = 2000
        self.MEASURE_LABEL = [100, 200, 500, 1000, 1100, 1200, 1600, 1700, 1800, 1900, 2000]

    @staticmethod
    def erase_test(_dict, keys):
        worst_time, best_time = 0, 1e9
        index = [0, len(keys) // 2, len(keys) - 1]
        for i in index:
            dict_copy = copy.deepcopy(_dict)
            measurement_started = time.time()
            dict_copy.erase(keys[i])
            time_spent = time.time() - measurement_started
            worst_time = max(worst_time, time_spent)
            best_time = min(best_time, time_spent)
        return worst_time, best_time
