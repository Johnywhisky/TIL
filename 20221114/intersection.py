import random
import time
from typing import List


def intersection_filter(l1: List[int], l2: List[int]) -> List[int]:
    """
    Time Complexity: O(n^2)
    """
    s = time.time()
    ans = list(filter(lambda x: x in l1, l2))
    print(time.time() - s)
    return ans


def intersection_filter_with_set(l1: List[int], l2: List[int]) -> List[int]:
    """
    Time Complexity: O(2n)
    """
    s = time.time()
    ans = list(filter(set(l1).__contains__, l2))
    print(time.time() - s)
    return ans


def intersection_set(l1: List[int], l2: List[int]) -> List[int]:
    """
    Time Complexity: O(2n)
    """
    s = time.time()
    ans = set(l1).intersection(l2)
    print(time.time() - s)
    return ans


r = list(range(1, 100000))
l1 = list(random.choices(r, k=10000))
l2 = list(random.choices(r, k=10000))
intersection_filter(l1, l2)
intersection_filter_with_set(l1, l2)
intersection_set(l1, l2)
