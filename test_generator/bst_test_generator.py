from collections import namedtuple
import test_generator.random_test_generator as generator
case = namedtuple('Case', ['dict_type', 'worst', 'best'])


def worst_case(n):
    return [x for x in range(n)]


def random_case(n):
    return generator.generate(n)


def construct_input_for_balanced_tree(left, right, best):
    if right - left > 1:
        middle = (left + right) // 2
        best.append(middle)
        construct_input_for_balanced_tree(left, middle, best)
        construct_input_for_balanced_tree(middle, right, best)


def best_case(n):
    best_order = []
    construct_input_for_balanced_tree(0, n + 1, best_order)
    return best_order


def generate(n):
    return case('bst', worst_case(n), best_case(n))
