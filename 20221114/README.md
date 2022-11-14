# algorithm
누적합 알고리즘
그리디 알고리즘
이분 탐색 알고리즘
브루트포스 알고리즘

# Sort

## Bubble Sort
``` python
def bubble_sort(data: List[int]) -> List[int]:
    length = len(data)
    for idx in range(length - 1):
        swap = False
        for inner_idx in range(length - idx - 1):
            if (f := data[inner_idx]) > (b := data[inner_idx + 1]):
                data[inner_idx], data[inner_idx + 1] = b, f
                swap = True
        if swap is False:
            print(f"{time.time() - s} s")
            return data
    return data
```
|   이름   |                    시간복잡도                    |   소요시간    |
|:------:|:-------------------------------------------:|:---------:|
| 버블 정렬  |           O(n) ~ O(n<sup>2</sup>)           |  0.0357s  |



## Insertion Sort
``` python
def insertion_sort(data: List[int]) -> List[int]:
    for idx in range(len(data) - 1):
        for inner_idx in range(idx + 1, 0, -1):
            if (b := data[inner_idx]) < (f := data[inner_idx - 1]):
                data[inner_idx - 1], data[inner_idx] = b, f
            else:
                break
    return data
```
|   이름   |                    시간복잡도                    |   소요시간    |
|:------:|:-------------------------------------------:|:---------:|
| 삽입 정렬  |           O(n) ~ O(n<sup>2</sup>)           | 0.0230s |


## Selection Sort
``` python
def selection_sort(data: List[int]) -> List[int]:
    length = len(data)
    for idx in range(length - 1):
        lowest_idx = idx
        for inner_idx in range(idx + 1, length):
            if data[inner_idx] < data[lowest_idx]:
                lowest_idx = inner_idx
        data[lowest_idx], data[idx] = data[idx], data[lowest_idx]
    return data
```
|  이름   |                    시간복잡도                    |   소요시간    |
|:-----:|:-------------------------------------------:|:---------:|
| 선택 정렬 |           O(n) ~ O(n<sup>2</sup>)           | 0.018s |
