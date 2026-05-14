def twoSum(nums, target):
    # מילון לשמירת ערכים שראינו והאינדקס שלהם
    # Key: המספר שחסר לנו (Complement), Value: האינדקס של המספר הנוכחי
    seen = {}
    
    for i, num in enumerate(nums):
        if num in seen:
            # מצאנו את המספר שחיכינו לו!
            return [seen[num], i]
        
        # אנחנו שומרים את מה שחסר לנו כדי להגיע ל-target
        complement = target - num
        seen[complement] = i