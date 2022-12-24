from collections import deque, defaultdict, Counter
import itertools
import re
from typing import TypeVar, Generator, Iterable, Tuple, List

_T = TypeVar("T")

def adjacent_pairs(elements: Iterable[_T]) -> Generator[Tuple[_T, _T], None, None]:
    elements_iter = iter(elements)
    last_element = next(elements_iter)
    for element in elements_iter:
        yield (last_element, element)
        last_element = element

def all_pairs(elements: Iterable[_T]) -> Generator[Tuple[_T, _T], None, None]:
    elements_list = list(elements)
    for i in range(len(elements_list)):
        for j in range(i + 1, len(elements_list)):
            yield (elements_list[i], elements_list[j])

def all_tuples(elements: Iterable[_T]) -> Generator[Tuple[_T, _T], None, None]:
    elements_list = list(elements)
    for i in range(len(elements_list)):
        for j in range(len(elements_list)):
            if j == i: continue
            yield (elements_list[i], elements_list[j])


# yes, everyone else calls this "cumsum" but ohwell
def rolling_sum(elements: Iterable[_T], start: _T = None) -> List[_T]:
    rsum = []
    elements_iter = iter(elements)
    
    if start is None:
        rsum.append(next(elements_iter))
    else:
        rsum.append(start)
    
    for element in elements_iter:
        rsum.append(rsum[-1] + element)
    return rsum


# I did some rough experiments with this version vs. a version that uses a deque, which
# has efficient popleft, and it seems like this version actually wins because of how slow
# iterating over a deque is (which you have to do if you want to use the results)
def rolling_window(
    elements: Iterable[_T],
    window_size: int,
) -> Generator[Tuple[_T, ...], None, None]:
    current_window = []
    for element in elements:
        current_window.append(element)
        if len(current_window) > window_size:
            del current_window[0]
        if len(current_window) == window_size:
            yield current_window



# this is like slightly borked because it doesn't get negative numbers
# oh well i guess
#nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

def nums(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]

def numsp(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]

def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


# underscored names are in case functions get shadowed by accident
adjp = _adjp = adjacent_pairs
ap = _ap = all_pairs
at = _at = all_tuples
rw = _rw = rolling_window
rsum = _rsum = rolling_sum

dd = _dd = defaultdict
ctr = _ctr = Counter
