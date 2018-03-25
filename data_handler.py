import matplotlib.pyplot as plot
import matplotlib.patches as patches
import numpy
import os
from collections import namedtuple
Data = namedtuple('Data', ['dict_name', 'test_name',
                           'query_type', 'ox_data', 'oy_data', 'delta'])

delta_coef = {6: 2.5706, 11: 2.281, 16: 2.1314, 21: 2.0860, 26: 2.0555, 31: 2.0423,
              36: 2.0301, 41: 2.0211, 51: 2.0086, 101: 1.9840}
TEST_DIR = os.getcwd() + '/results'
TIME_FACTOR = 10 ** 6


def calculate_coef(x, y):
    k = ((sum(x) * sum(y) - len(x) * numpy.dot(x, y)) /
         (sum(x) ** 2 - len(x) * sum(map(lambda val: val ** 2, x))))
    b = (sum(y) - k * sum(x)) / len(x)
    return k, b


def calculate_s_and_delta(measurement_data):
    n = len(measurement_data)
    sum_data = sum(measurement_data)
    average = sum_data / n
    result = 0
    for y in measurement_data:
        result += (y - average) ** 2
    s = (result / (n - 1)) ** 0.5
    delta = delta_coef[n] * s / (n ** 0.5)
    return s, delta


def insert_data_collector(path):
    dummy, dict_name, other_info = path.rsplit('/', maxsplit=2)
    query_type, test_name = other_info.split('@')
    if query_type != 'insert':
        return []
    iterations_data_y = []
    iterations_data_x = []
    with open(path, 'r') as f:
        for line in f:
            if line.find('Iteration') != -1:
                iterations_data_x.append([])
                iterations_data_y.append([])
                continue
            splitted = line.split()
            x = int(splitted[0][:-2])
            y = float(splitted[3])
            iterations_data_x[len(iterations_data_x) - 1].append(x)
            iterations_data_y[len(iterations_data_y) - 1].append(y)
    return process(dict_name, iterations_data_x, iterations_data_y, query_type, test_name)


def process(dict_name, iterations_data_x, iterations_data_y, query_type, test_name):
    oy = []
    delta = []
    for i in range(len(iterations_data_y[0])):
        current_measurement = []
        for j in (range(len(iterations_data_y))):
            current_measurement.append(iterations_data_y[j][i])
        s, current_delta = calculate_s_and_delta(current_measurement)
        oy.append(s * TIME_FACTOR)
        delta.append(current_delta)
    return Data(dict_name, test_name,
                          query_type, iterations_data_x[0], oy, delta)


def erase_find_data_collector(path, is_best_case):
    dummy, dict_name, other_info = path.rsplit('/', maxsplit=2)
    query_type, test_name = other_info.split('@')
    if query_type != 'erase' and query_type != 'find':
        return []
    query_type += '_best' if is_best_case else '_worst'
    iterations_data_y = []
    iterations_data_x = []
    with open(path, 'r') as f:
        for line in f:
            if line.find('Iteration') != -1:
                iterations_data_x.append([])
                iterations_data_y.append([])
                continue
            splitted = line.split()
            x = int(splitted[1])
            data_index = 5 if is_best_case else 3
            y = float(splitted[data_index])
            iterations_data_x[len(iterations_data_x) - 1].append(x)
            iterations_data_y[len(iterations_data_y) - 1].append(y)
    return process(dict_name, iterations_data_x, iterations_data_y, query_type, test_name)


def collect_data(path):
    data = []
    insert_data = insert_data_collector(path)
    if len(insert_data) > 0:
        data.append(insert_data_collector(path))
    other_data_best = erase_find_data_collector(path, True)
    if len(other_data_best) > 0:
        data.append(other_data_best)
    other_data_worst = erase_find_data_collector(path, False)
    if len(other_data_worst) > 0:
        data.append(other_data_worst)
    return data


def build_graph():
    results = []
    for address, directories, files in os.walk(TEST_DIR):
        for file in files:
            data = collect_data(address + '/' + file)
            results.extend(collect_data(address + '/' + file))
    for result in results:
        plot.clf()
        plot.errorbar(result.ox_data, result.oy_data, yerr=result.delta,
                      fmt='or', ecolor='r')
        x_ap = numpy.logspace(numpy.log10(min(result.ox_data)),
                              numpy.log10(max(result.ox_data)), 200)
        if max(result.oy_data) > min(result.oy_data) * 5:
            k, b = calculate_coef(result.ox_data, result.oy_data)
            y_ap = list(map(lambda x: k * x + b, x_ap))
        else:
            k, b = calculate_coef(list(map(numpy.log10, result.ox_data)), result.oy_data)
            y_ap = list(map(lambda x: k * numpy.log10(x) + b, x_ap))
        plot.plot(x_ap, y_ap, 'b')
        plot.yscale('log')
        plot.xscale('log')
        plot.xlabel('Размер словаря')
        plot.ylabel('Время выполнения, мкс')
        red_label = patches.Patch(color='r', label='Результаты тестирования')
        green_label = patches.Patch(color='b', label='Апроксимация')
        plot.legend(handles=[red_label, green_label], loc=2)
        plot.title('{0}:{1}@{2}'.format(result.dict_name, result.test_name, result.query_type))
        plot.axis([0, max(result.ox_data) * 1.5, 0, max(result.oy_data) * 1.5])
        plot.savefig('graphs/{0}:{1}@{2}.png'.format(result.dict_name,
                                                     result.test_name,
                                                     result.query_type), bbox_inches='tight')


def main():
    build_graph()

if __name__ == '__main__':
    main()