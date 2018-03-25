import os
import random
from collections import namedtuple

case = namedtuple('Case', ['dict_type', 'worst', 'random', 'best'])
TEST_DIR = os.getcwd()[:-14] + 'tests/'
random.seed()


def generate(n):
    used_keys = set()
    while len(used_keys) < n:
        key = random.randint(1, 1e18)
        if key not in used_keys:
            used_keys.add(key)
    return list(used_keys)


def generate_all_cases_are_random(n):
    random_case = generate(n)
    return case('random', random_case, random_case, random_case)