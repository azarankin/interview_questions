
#loop o(n) version
def getMaximumLength(sensorData):
    #sensorData = arr[] {0, 10, 31, 0, 2, 0, 6, 0 }
    first_occurrence = {}
    current_diff = 0
    max_len = 0
    
    for i, val in enumerate(sensorData):
        if val > 0:
            current_diff += 1
        else:
            current_diff -= 1
            
        if current_diff == 1:
            max_len = i + 1
            
        target = current_diff - 1
        if target in first_occurrence:
            length = i - first_occurrence[target]
            if length > max_len:
                max_len = length
        
        if current_diff not in first_occurrence:
            first_occurrence[current_diff] = i
            
    return max_len     
                
    
    
    



#loop o(n^2) version
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