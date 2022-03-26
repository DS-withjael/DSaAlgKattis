from itu.algs4.sorting.insertion_sort import sort, _less
from typing import List, TypeVar

T = TypeVar("T")

def sort(a: List[T]):
    """Rearranges the array in ascending order, using the natural order.
    :param a: the array to be sorted.
    """
    # Sort a[] into increasing order.
    N = len(a)
    for i in range(1, N):
        # Insert a[i] among a[i-1], a[i-2], a[i-3]...
        for j in range(i, 0, -1):
            if not _less(a[j], a[j - 1]):
                break
            _exch(a, j, j - 1)


def _less(v: T, w: T):
    if v == "F" and w == "FX":
        return False
    return v < w


def _exch(a: List[T], i: int, j: int):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def sort_std():
    no_of_std = int(input())
    dct = {}
    
    for i in range(0,no_of_std):
        std = input().split()
        dct.setdefault(std[1], []).append(std[0])
        
    grades = list(dct.keys())
    sort(grades)
    
    for i in grades:
        elements = dct[i]
        sort(elements)
        for j in elements:
            print(j)


sort_std()
