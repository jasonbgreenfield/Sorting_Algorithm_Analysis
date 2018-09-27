from bubble import bubble_sort
from insertion import insertion_sort
from merge import merge_sort

def test_1(sorter, name):

    # checks when the list is empty
    a = []

    try:
        sorter(a)
    except Exception:
        print(f"{name} failed with an empty list.")


def test_2(sorter, name):

    # checks when the list has only one element
    a = [1]

    try:
        sorter(a)
    except Exception:
        print(f"{name} failed when list has one element.")


def test_3(sorter, name):

    # checks when list has multiple different types of objects
    a = [2, "hello", 3.141]

    try:
        sorter(a)

    except Exception:
        print(f"{name} failed when list contains multiple different types of objects.")


def test_4(sorter, name):

    # checks when list is not a list
    a = 2

    try:
        sorter(a)

    except Exception:
        print(f"{name} failed when list is a different variable type.")


def run_tests(sorter, name):

    test_1(sorter, name)

    test_2(sorter, name)

    test_3(sorter, name)

    test_4(sorter, name)


if __name__ == "__main__":

    run_tests(bubble_sort, name= "bubble")

    run_tests(insertion_sort, name = "insertion_sort")

    run_tests(merge_sort, name= "merge_sort")