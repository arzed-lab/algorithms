from typing import List

A = [64,25,12,22,11,555]
# Traverse through all array elements
def selection_sort(A:List) -> List:
    for i in range(len(A)):
        min_index = i
        # Find the minimum element in remaining 
        # unsorted array
        for j in range(i+1, len(A)):
            if A[min_index] > A[j]:
                min_index = j
        # Swap the found minimum element with 
        # the first element 
        A[i], A[min_index] = A[min_index], A[i]
    return A

def bubble_sort(B: List) -> List:
    size_n = len(B)
    # Traverse through all array elements
    for i in range(size_n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, size_n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if B[j] > B[j+1]:
                B[j], B[j + 1] = B[j + 1], B[j]
    return B



print(bubble_sort(A))