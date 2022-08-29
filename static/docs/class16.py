"""
class16.py

Cost
"""

def list_accumulator(fn, lst, base):
    result = base
    for el in lst:
        result = fn(result, el)
    return result
    
def list_map(fn, lst):
    return list_accumulator(lambda lst, e: lst + [fn(e)],
                            lst, [])


### Edit distance (from project 2 and class13)

import sys, time

sys.setrecursionlimit(25000)

def memoize(function):
    """ Memoization decorator for a function taking one or more arguments. """
    class Memodict(dict):
        """
        memodict class
        """
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = function(*key)
            return ret

    return Memodict().__getitem__

#@memoize
def edit_distance(a, b):
    """
    Returns the Levenshtein distance between a and b.
    """
    if not (a and b):
        return len(a) + len(b)
    else:
        if a[0] == b[0]:
            return edit_distance(a[1:], b[1:])
        else:
            return min(1 + edit_distance(a, b[1:]),     # insert
                       1 + edit_distance(a[1:], b),     # delete
                       1 + edit_distance(a[1:], b[1:])) # mutate

def time_execution(fn, n=1000):
    """
    Returns execution time of fn in milliseconds,
    averaged over n executions.
    """
    start_time = time.clock()    
    for _ in range(n):
        fn()
    stop_time = time.clock()
    # time.clock() returns seconds, convert to ms
    return 1000 * (stop_time - start_time) / n

def time_edit(mina = 8, maxa = 9, minb = 1, maxb = 10):
    for len1 in range(mina, maxa):
        for len2 in range(minb, maxb):
            s1 = 'a' * len1
            s2 = 'b' * len2
            ms = time_execution(lambda: edit_distance(s1, s2))
            print (("edit_distance({0:" + str(maxa) +
                   "}, {1:" + str(maxb) +
                   "}): {2:4f} ms").format(s1, s2, ms))

def test_edit():
    assert edit_distance('', '') == 0
    assert edit_distance('', 'one') == 3
    assert edit_distance('one', '') == 3
    assert edit_distance('bone', 'tone') == 1
    assert edit_distance('apple', 'fbi') == 5
    assert edit_distance('apple', 'orange') == 5
    assert edit_distance('abba', 'bba') == 1
    assert edit_distance('bba', 'abba') == 1
    print("Passed all tests!")

import timeit

def time_addition(ntrials = 1000000):
    print("1 + 1: " + str(timeit.timeit('1 + 1', number=ntrials)))
    

    
## some test lists

p = [1, 2, 3, 4]
q = [1, 2, 3, 4]

x1 = ['alpha', 'beta', 'gamma']


