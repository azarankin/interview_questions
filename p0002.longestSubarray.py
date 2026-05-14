def longestSubarray(arr):
    if not arr: 
        return 0
    
    num1, num2 = arr[0], None
    current_len = max_len = last_num_count = 0
    last_num = None

    for num in arr:
        if num == num1 or num == num2:
            current_len += 1
        '''elif num2 is None and abs(num - num1) <= 1: #לא חובה
            num2 = num
            current_len += 1'''
        else:
            if last_num is not None and abs(num - last_num) <= 1:
                num1, num2 = last_num, num
                current_len = last_num_count + 1
            else:
                num1, num2 = num, None
                current_len = 1
        
        if num == last_num:
            last_num_count += 1
        else:
            last_num = num
            last_num_count = 1
            
        max_len = max(max_len, current_len)
            
    return max_len  







# with sliding window
def longestSubarray(arr):
    n = len(arr)
    left = 0
    max_length = 0
    counts = {}
    
    for right in range(n):
        counts[arr[right]] = counts.get(arr[right], 0) + 1
        
        while len(counts) > 2 or (max(counts.keys()) - min(counts.keys()) > 1):
            # צמצום החלון מצד שמאל
            counts[arr[left]] -= 1
            if counts[arr[left]] == 0:
                del counts[arr[left]]
            left += 1
            
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            
    return max_length