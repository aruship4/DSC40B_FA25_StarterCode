def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    # TODO: Implement the assign_good_and_evil function
    
    labels = {}

    def opposite(label):
        return 'evil' if label == 'good' else 'good'
    
    for node in graph.nodes():
        if node not in labels:
            labels[node] = 'good'
            queue = deque([node])

            while queue:
                current = queue.popleft()
                current_label = labels[current]

                for neighbor in graph.neighbors(current):
                    if neighbor not in labels:
                        labels[neighbor] = opposite(current_label)
                        queue.append(neighbor)
                    elif labels[neighbor] == current_label:
                        return None
                    
    return labels
    
