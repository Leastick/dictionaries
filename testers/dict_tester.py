from dictionaries import dict_wrapper
import random
from testers import tester
import copy
import time

random.seed(1)


class DictTester(tester.Tester):
    def __init__(self, iter_amount, test_directory, result_directory):
        super().__init__(dict_wrapper.DictWrapper, iter_amount,
                         test_directory, result_directory + '/dict',
                         'dict')

    @staticmethod
    def erase_test(_dict, keys):
        worst_time, best_time = 0, 1e9
        for i in range(5):
            dict_copy = copy.deepcopy(_dict)
            measurement_started = time.time()
            dict_copy.erase(random.choice(keys))
            time_spent = time.time() - measurement_started
            worst_time = max(worst_time, time_spent)
            best_time = min(best_time, time_spent)
        return worst_time, best_time
