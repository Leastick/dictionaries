import argparse
import os
import sys
import time

from testers.bst_tester import BSTTester
from testers.list_tester import ListTester
from testers.sorted_list_tester import SortedListTester
from testers.treap_tester import TreapTester
from testers.hashtable_tester import HashtableTester
from testers.dict_tester import DictTester


TEST_DIR = os.getcwd() + '/tests/'
RESULTS_DIR = os.getcwd() + '/results/'
testers = (DictTester, ListTester, SortedListTester, TreapTester, BSTTester,
           lambda iter_amount, test_dir, result_dir, hash_func=hash: HashtableTester(
               iter_amount, test_dir, result_dir + 'hashtable/good_hash', hash_func),
           lambda iter_amount, test_dir, result_dir, hash_func=(lambda x: 5): HashtableTester(
                iter_amount, test_dir, result_dir + 'hashtable/bad_hash', hash_func))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('iter_amount', type=int,
                        help='количество запусков тестов на каждом наборе данных')
    return parser.parse_args(sys.argv[1:])


def main():
    parsed = parse()
    amount = parsed.iter_amount
    for tester_type in testers:
        iteration_started = time.time()
        tester = tester_type(amount, TEST_DIR, RESULTS_DIR)
        tester.start()
        print('\n{0} completed in {1} s'.format(tester.dict_name, time.time()
                                              - iteration_started))


if __name__ == '__main__':
    main()
