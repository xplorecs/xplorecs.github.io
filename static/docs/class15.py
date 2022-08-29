"""
class15.py

Generalizing List Functions
"""

def list_copy(lst):
    if not lst:
        return []
    else:
        return [lst[0]] + list_copy(lst[1:])

def list_addone(lst):
    if not lst:
        return []
    else:
        return [lst[0] + 1] + list_addone(lst[1:])

def list_map(fn, lst):
    if not lst:
        return []
    else:
        return [fn(lst[0])] + list_map(fn, lst[1:])

def list_map(fn, lst):
    result = []
    for e in lst:
        result.append(fn(e))
    return result

def list_map(fn, lst):
    return [fn(e) for e in lst]

def make_list_mapper(fn):
    def mapper(lst):
        return list_map(fn, lst)
    return mapper

def make_list_mapper(fn):
    return lambda lst: list_map(fn, lst)


### Mutators

def list_mutate_BAD(fn, lst):
    if not lst:
        pass
    else:
        lst[0] = fn(lst[0])
        list_mutate_BAD(fn, lst[1:])

def list_mutate(fn, lst):
    for i in range(len(lst)):
        lst[i] = fn(lst[i])

list_increment = lambda lst: list_mutate(lambda a: a + 1, lst)

def increment(a):
    return a + 1

def list_double(lst):
    list_mutate(lambda a: a * 2, lst)

def make_list_mutator(fn):
    def mutator(lst):
        list_mutate(fn, lst)
    return mutator

def make_list_mutator(fn):
    return lambda lst: list_mutate(fn, lst)

###

def list_accumulator(fn, lst, base):
    result = base
    for el in lst:
        result = fn(result, el)
    return result
    
def list_map(fn, lst):
    def appender(lst, e):
        return lst + [fn(e)]
    return list_accumulator(appender, lst, [])


## some test lists

p = [1, 2, 3, 4]
q = [1, 2, 3, 4]

x1 = ['alpha', 'beta', 'gamma']


