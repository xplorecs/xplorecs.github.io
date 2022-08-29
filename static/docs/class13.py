def hamming_distance_rec(s1, s2):
    """
    Returns the hamming distance between s1 and s2.
    Requires s1 and s2 have the same length.
    """
    assert len(s1) == len(s2)
    if not s1:
        return 0
    else:
        return (not s1[0] == s2[0]) \
            + hamming_distance_rec(s1[1:], s2[1:])

def hamming_distance_loop(s1, s2):
    assert len(s1) == len(s2)
    count = 0
    for i in range(len(s1)):
        count = count + (not s1[i] == s2[i])
    return count

def hamming_distance_lc(s1, s2):
    assert len(s1) == len(s2)
    return sum([not e1 == e2 \
                for (e1, e2) in zip(s1, s2)])

hamming_distance = hamming_distance_lc

def test_hamming():
    assert hamming_distance("","") == 0
    assert hamming_distance("a", "a") == 0
    assert hamming_distance("a", "b") == 1
    assert hamming_distance("aaa", "aba") == 1
    assert hamming_distance("abababa", "abacabb") == 2
    assert hamming_distance("abcdefg", "bcdefgh") == 7
    print("All tests passed!")

import sys, time, random, string

sys.setrecursionlimit(50000)

def random_bases(n):
    return ''.join(random.choice(['A','C','G','T']) for i in range(n))

def time_hamming(n):
    s1 = random_bases(n)
    s2 = random_bases(n)
    for impl in [hamming_distance_rec,
                 hamming_distance_loop,
                 hamming_distance_lc]:
        start_time = time.clock()

        for _ in range(1000):
            impl(s1, s2)
        stop_time = time.clock()
        print("Time for " + impl.__name__ + ": " +
              str(stop_time - start_time))

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

def edit_distance(a, b):
    if not (a and b):
        return len(a) + len(b)
    return min(1 + edit_distance(a, b[1:]),     # insert
               1 + edit_distance(a[1:], b),     # delete
               (0 if a[0] == b[0] else 1) + edit_distance(a[1:], b[1:]))

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

## Nested Lists

def list_copy(lst):
    """
    Returns a shallow copy of the input lst.
    """
    if not lst:
        return []
    else:
        return [lst[0]] + list_copy(lst[1:])

def is_list(obj):
    """
    Returns True iff obj is a list.
    """
    return isinstance(obj, list)    
    
def list_deep_copy(lst):
    """
    Returns a deep copy of the input list.
    """
    if not lst:
        return []
    elif is_list(lst[0]):
        return [list_deep_copy(lst[0])] + list_deep_copy(lst[1:])
    else:
        return [lst[0]] + list_deep_copy(lst[1:])
    
def list_flatten(lst):
    if not lst:
        return []
    elif is_list(lst[0]):
        return list_flatten(lst[0]) + list_flatten(lst[1:])
    else:
        return [lst[0]] + list_flatten(lst[1:])
    


    
    





    
