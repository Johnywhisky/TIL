import random
import time

from typing import List

"""
Bubble Sort(버블 정렬)
Time Complexity: O(n^2) best O(n) when list already sorted

Insertion Sort(삽입 정렬)
Time Complexity: O(n^2) best O(n) when list already sorted

Selection Sort(선택 정렬)
Time Complexity: O(n^2) best O(n) when list already sorted
"""


def bubble_sort(array: List[int]) -> List[int]:
    length = len(array)
    s = time.time()
    for idx in range(length - 1):
        swap = False
        for inner_idx in range(length - idx - 1):
            if (f := array[inner_idx]) > (b := array[inner_idx + 1]):
                array[inner_idx], array[inner_idx + 1] = b, f
                swap = True
        if swap is False:
            print(f"{time.time() - s} s")
            return array
    print(f"{time.time() - s} s")
    return array


data = random.sample(range(10000), 1000)
bubble_res = bubble_sort(data)


def insertion_sort(array: List[int]) -> List[int]:
    s = time.time()
    for idx in range(len(array) - 1):
        for inner_idx in range(idx + 1, 0, -1):
            if (b := array[inner_idx]) < (f := array[inner_idx - 1]):
                array[inner_idx - 1], array[inner_idx] = b, f
            else:
                break
    print(f"{time.time() - s} s")
    return array


data = random.sample(range(10000), 1000)
insertion_res = insertion_sort(data)


def selection_sort(array: List[int]) -> List[int]:
    length = len(array)
    s = time.time()
    for idx in range(length - 1):
        lowest_idx = idx
        for inner_idx in range(idx + 1, length):
            if array[inner_idx] < array[lowest_idx]:
                lowest_idx = inner_idx
        array[lowest_idx], array[idx] = array[idx], array[lowest_idx]

    print(f"{time.time() - s} s")
    return array


data = random.sample(range(10000), 1000)
selection_res = selection_sort(data)


def check_is_sorted(sorted_list: List[int]) -> bool:
    for idx, el in enumerate(sorted_list[:-2]):
        if el > sorted_list[idx + 1]:
            return False
    return True


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
