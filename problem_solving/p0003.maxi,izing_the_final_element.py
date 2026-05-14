def getMaxValue(arr):
    # Sort the array to handle elements greedily
    arr.sort()
    
    # Condition 1: The first element must be 1
    current_max = 1
    
    # Condition 2: arr[i] - arr[i-1] <= 1
    # We skip the first element (already set to 1) and iterate through the rest
    for i in range(1, len(arr)):
        # If the current element is greater than the previous + 1,
        # we "reduce" it to the maximum allowable value (current_max + 1).
        # Otherwise, if it's already smaller or equal, we can't make it larger
        # than its original value.
        if arr[i] > current_max:
            current_max += 1
            
    return current_max