from collections import namedtuple
import test_generator.random_test_generator as generator
case = namedtuple('Case', ['dict_type', 'worst', 'random', 'best'])


def worst_case(n):
    return [x for x in range(n - 1, 0, -1)]


def random_case(n):
    return generator.generate(n)


def best_case(n):
    return [x for x in range(n)]


def generate(n):
    return case('sorted_list', worst_case(n), random_case(n), best_case(n))
