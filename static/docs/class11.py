"""
class11.py

This includes answers to some of the problems, so try them on your own 
first before looking at my code.
"""

# This is the pair and list-making code from Class 9.

def make_pair(a, b):
    return [a, b]

def pair_first(pair):
    return pair[0]

def pair_last(pair):
    return pair[1]

def is_pair(pair):
    return type(pair) == list and len(pair) == 2

# Making pairs without Lists!

def make_pair(a, b):
    def selector(which):
        if which:
            return a
        else:
            return b
    return selector

def pair_first(pair):
    return pair(True)

def pair_last(pair):
    return pair(False)

# A list is a pair where the second part is a list,
#          or None

def make_list(first, second):
    return make_pair(first, second)

def list_first(lst):
    return pair_first(lst)

def list_rest(lst):
    return pair_last(lst)

###

def list_increment(lst):
    """
    Returns a new list that contains all the elements in the input
    list incremented by 1.

    For example, list_increment([1, 2, 3]) should return [2, 3, 4].
    """

    # recursive version
    if not lst:
        return []
    else:
        return [lst[0] + 1] + list_increment(lst[1:])

def list_double(lst):
    """
    Returns a new list that contains all the elements in the input
    list doubled.

    For example, list_double([1, 2, 3]) should return [2, 4, 6].
    """

    # recursive version
    if not lst:
        return []
    else:
        return [lst[0] * 2] + list_double(lst[1:])


def list_map(fn, lst):
    """
    Returns a new list that contains the result of applying fn
    to each elements in the input list.

    For example, list_map(abs, [1, -2, 3]) should return [1, 2, 3].
    """

    # recursive version
    if not lst:
        return []
    else:
        return [fn(lst[0])] + list_map(fn, lst[1:])
    
### Return the length of the input list

def list_length(lst):
    if lst == None:
        return 0
    else:
        return 1 + list_length(list_rest(lst))
    
def plst_length(lst):
    if not lst:
        return 0
    else:
        return 1 + plst_length(lst[1:])

def pclst_length(lst):
    return sum([1 for e in lst])

# Of course, best to just use built-in len(lst).

# Returns True iff the input is a list.

def is_list(obj):
    if obj == None:
        return True
    else:
        if is_pair(obj):
            return is_list(pair_last(obj))
        else:
            return False

def list_sum(lst):
    if lst == None:
        return 0
    else:
        return list_first(lst) + list_sum(list_rest(lst))

def list_max(lst):
    if list_length(lst) == 1:
        return list_first(lst)
    else:
        return max(list_first(lst),
                   list_max(list_rest(lst)))
    
def test_list():
    chief_officers = make_list('Washington',
                               make_list('Hamilton',
                                         make_list('Wilkinson',
                                                   make_list('Dearborn',
                                                             make_list('Brown',
                                                                       None)))))
    assert is_list(None)
    assert is_list(chief_officers)
    assert not is_list(3)
    assert not is_list(make_pair(1, 2))
    assert is_list(make_pair(3, None))

    assert list_length(None) == 0
    assert list_length(chief_officers) == 5
    assert list_sum(None) == 0

    l123 = make_list(1, make_list(2, make_list(3, None)))
    lsqueeze = make_list(8,
                         make_list(5,
                                   make_list(3,
                                             make_list(5,
                                                       make_list(9,
                                                                 make_list(3,
                                                                           make_list(7, None)))))))
    assert list_sum(l123) == 6
    assert list_max(l123) == 3
    assert list_sum(lsqueeze) == sum([8, 5, 3, 5, 9, 3, 7])
    assert list_max(lsqueeze) == 9
                                                            
    print("Finished all tests!")
        
    


        
