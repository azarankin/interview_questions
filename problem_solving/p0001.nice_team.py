
def maxPairs(skillLevel, minDiff):
    # Write your code here
    skillLevel.sort()
    n = len(skillLevel)
    left = 0
    right = n // 2  # מתחילים מהחצי כדי לאפשר מקסימום זוגות
    count = 0
    
    while left < n // 2 and right < n:
        if skillLevel[right] - skillLevel[left] >= minDiff:
            count += 1
            left += 1
            right += 1
        else:
            # ההפרש קטן מדי, חייבים שחקן חזק יותר מימין
            right += 1
            
    return count