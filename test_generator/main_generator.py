import sys
import argparse
import os
import random
from collections import namedtuple
import test_generator.bst_test_generator as bst
import test_generator.random_test_generator as random_generator
import test_generator.sorted_list_test_generator as sorted_list


case = namedtuple('Case', ['dict_type', 'worst', 'random', 'best'])
TEST_DIR = os.getcwd()[:-14] + 'tests/'
random.seed()


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='n is size of dict')
    parser.add_argument('--bst', action='store_true',
                        help='генерирует тесты для  bst')
    parser.add_argument('--hashtable', action='store_true',
                        help='генерирует тесты для hashtable')
    parser.add_argument('--list', action='store_true',
                        help='генерирует тесты для словаря на основе списка')
    parser.add_argument('--sorted_list', action='store_true',
                        help='генерирует тесты для словаря на отсортированном списке')
    parser.add_argument('--treap', action='store_true',
                        help='генерирует тесты для декартова дерева')
    return parser.parse_args(sys.argv[1:])


def init_generators(parsed):
    generators = set()
    if parsed.bst:
        generators.add(bst.generate)
    if parsed.hashtable:
        generators.add(lambda n:
                       random_generator.generate_all_cases_are_random(n))
    if parsed.treap:
        generators.add(lambda n:
                       random_generator.generate_all_cases_are_random(n))
    if parsed.list:
        generators.add(lambda n:
                       random_generator.generate_all_cases_are_random(n))
    if parsed.sorted_list:
        generators.add(sorted_list.generate)
    return list(generators)


def save_case(test_case):
    if test_case.dict_type == 'random':
        save_test(test_case.dict_type + '_test', test_case.random)
    else:
        save_test(test_case.dict_type + '_worst', test_case.worst)
        save_test(test_case.dict_type + '_best', test_case.best)


def save_test(filename, keys):
    with open(TEST_DIR + filename, 'w') as f:
        for key in keys:
            f.write('{}\n'.format(key))


def main():
    parsed = parse()
    generators = init_generators(parsed)
    n = parsed.n
    for generator in generators:
        save_case(generator(n))


if __name__ == '__main__':
    main()