def getMaximumLength(sensorData):
    #sensorData = arr[] {0, 10, 31, 0, 2, 0, 6, 0 }
    n = len(sensorData)
    max_len = 0
    
    for start in range(n):
        signals = 0
        zeros = 0
        for end in range(start, n):
            if sensorData[end] > 0:
                signals += 1
            else:
                zeros += 1
            if signals - zeros == 1:
                current_length = end - start + 1
                if current_length > max_len:
                    max_len = current_length
 
    return max_len