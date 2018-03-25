import time
import os
import abc
import random


class Tester:
    def __init__(self, dict_type, iter_amount, test_directory, result_directory,
                 dict_name, hash_func=None):
        self.dict_type = dict_type
        self.iter_amount = iter_amount
        self.test_directory = test_directory
        self.result_directory = result_directory
        self.dict_name = dict_name
        self.MAX_ITERATIONS = 1e9
        self.MEASURE_LABEL = [100, 1500, 5000, 10_000, 15_000, 50_000, 70_000, 80_000,
                              90_000, 95_000, 100_000]
        self.hash_func = hash_func

    @staticmethod
    def insert_test(_dict, key):
        measurement_started = time.time()
        _dict.insert(key, 1)
        return time.time() - measurement_started

    @staticmethod
    def find_test(_dict, keys):
        longest, shortest = 0, 1e9
        for key in keys:
            measurement_started = time.time()
            _dict.contains_key(key)
            time_spent = time.time() - measurement_started
            longest = max(longest, time_spent)
            shortest = min(shortest, time_spent)
        return longest, shortest

    @staticmethod
    @abc.abstractmethod
    def erase_test(_dict, keys):
        pass

    def create_dict(self):
        if self.hash_func is not None:
            return self.dict_type(self.hash_func)
        else:
            return self.dict_type()

    def warm_up(self, keys):
        random.shuffle(keys)
        for i in range(3):
            _temp_dict = self.create_dict()
            for index, key in enumerate(keys):
                if index > self.MAX_ITERATIONS:
                    continue
                _temp_dict.insert(key, 1)

    def run(self, iteration):
        for address, directories, files in os.walk(self.test_directory):
            for file in files:
                _dict = self.create_dict()
                with open(address + file, 'r') as f, \
                        open('{0}/insert@{1}'.format(self.result_directory,
                                                     file), 'a') as insert, \
                        open('{0}/find@{1}'.format(self.result_directory,
                                                   file), 'a') as find, \
                        open('{0}/erase@{1}'.format(self.result_directory,
                                                    file), 'a') as erase:
                    current_keys = []
                    insert.write('Iteration #{}\n'.format(iteration))
                    find.write('Iteration #{}\n'.format(iteration))
                    erase.write('Iteration #{}\n'.format(iteration))
                    keys = [int(x) for x in f]
                    self.warm_up(keys)
                    for index, key in enumerate(keys):
                        key = int(key)
                        if index > self.MAX_ITERATIONS:
                            break
                        current_keys.append(key)
                        if index + 1 in self.MEASURE_LABEL:
                            insert_time = self.insert_test(_dict, key)
                            insert.write('{0}th element at {1} sec\n'.format(index + 1, insert_time))
                            worst_find_time, best_find_time = self.find_test(_dict, current_keys)
                            find.write('Amount: {0} worst: {1} best: {2}\n'.format(index + 1,
                                                                                   worst_find_time,
                                                                                   best_find_time))
                            worst_erase_time, best_erase_time = self.erase_test(_dict, current_keys)
                            erase.write('Amount: {0} worst: {1} best: {2}\n'.format(index + 1,
                                                                                    worst_erase_time,
                                                                                    best_erase_time))
                        else:
                            _dict.insert(key, 1)

    def start(self):
        for iteration_number in range(self.iter_amount):
            self.run(iteration_number)
