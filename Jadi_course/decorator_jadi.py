"""
Definition of a custom decorator
"""
import datetime


def calc_func_time(func):
    """
    Calculate time of running function
    """
    def wrapper(n):
        start_time = datetime.datetime.now()
        func(n)
        end_time = datetime.datetime.now()

        result = end_time.second - start_time.second
        print(f"Time of running function {result}(sec)")

    return wrapper


@calc_func_time
def create_list(n):
    """
    Create list from 1 to n
    """
    my_list = []
    for i in range(1, n + 1):
        my_list.append(i)


create_list(46545445)
