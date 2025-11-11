import random

def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    # TODO: Implement the knn_distance function

    
    distances = [(abs(x - q), x) for x in arr]
    
    distances.sort(key=lambda t: t[0])
    
    kth_distance, kth_point = distances[k - 1]
    
    return (kth_distance, kth_point)


