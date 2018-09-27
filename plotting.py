import numpy as np
import matplotlib.pyplot as plt
import random
import time
from bubble import bubble_sort
from insertion import insertion_sort
from merge import merge_sort


def run_tests(sorter, lengths):

    to_test = []

    for length in lengths:

        temp = []

        for j in range(length):

            temp.append(random.randint(0, 1000000))

        to_test.append(temp)

    results = []

    for test in to_test:

        total_time = 0

        for j in range(3):

            list = test

            start_time = time.time()

            sorted = sorter(list)

            total_time = total_time + (time.time() - start_time)

        results.append( [len(test), total_time/3])

    return results

def plot(bubble, insertion, merge):

    bubble = np.array(bubble)
    insertion = np.array(insertion)
    merge = np.array(merge)

    bubble_x, bubble_y = bubble.T
    insertion_x, insertion_y = insertion.T
    merge_x, merge_y = merge.T

    plt.scatter(bubble_x, bubble_y)
    plt.scatter(insertion_x, insertion_y)
    plt.scatter(merge_x, merge_y)

    plt.xlabel('Length of list')
    plt.ylabel('Time to sort')
    plt.legend(('Bubble Sort', 'Insertion Sort', 'Merge Sort'))
    plt.show()

def run():

    bubble_results = run_tests(bubble_sort, [100, 1000, 5000, 10000, 25000, 75000])

    insertion_results = run_tests(insertion_sort, [1000, 10000, 25000, 100000, 250000, 500000])

    merge_results = run_tests(merge_sort, [1000, 10000, 25000, 100000, 250000, 500000])

    plot(bubble_results, insertion_results, merge_results)

if __name__ == "__main__":

    run()



