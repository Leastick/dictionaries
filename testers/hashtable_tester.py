import copy
import time
from dictionaries import hashtable
from testers import tester


class HashtableTester(tester.Tester):
    def __init__(self, iter_amount, test_directory, result_directory, hash_func):
        self.suffix = result_directory.rsplit('/',maxsplit=1)[1]
        super().__init__(hashtable.HashTable, iter_amount,
                         test_directory, result_directory,
                         'hashtable_' + self.suffix, hash_func)
        if self.suffix == 'bad_hash':
            self.MAX_ITERATIONS = 2000
            self.MEASURE_LABEL = [100, 200, 500, 1000, 1100, 1200, 1600, 1700, 1800, 1900, 2000]

        else:
            self.MAX_ITERATIONS = 10000
            self.MEASURE_LABEL = [100, 200, 500, 1000,
                                  1100, 1200, 1600, 1700,
                                  1800, 1900, 2000, 3500,
                                  4000, 5000, 6000, 7000,
                                  8000, 9600, 9700, 9800,
                                  9900, 10_000]

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
