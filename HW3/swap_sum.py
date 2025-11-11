def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    # TODO: Implement the swap_sum function
    
    sumA = sum(A)
    sumB = sum(B)
    delta = sumB - sumA - 10
    if delta % 2 != 0:
        return None
    d = delta // 2

    i = 0
    j = 0
    n, m = len(A), len(B)
    while i < n and j < m:
        diff = B[j] - A[i]
        if diff == d:
            return (i, j)
        elif diff < d:
            j += 1
        else:
            i += 1

    return None

