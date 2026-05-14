#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxArea' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. BOOLEAN_ARRAY isVertical
#  4. INTEGER_ARRAY distance
#


import bisect
import heapq

def getMaxArea(w, h, isVertical, distance):
    # 1. אתחול קווים (כולל הגבולות של המלבן)
    h_lines = [0, h]
    v_lines = [0, w]
    
    # 2. אתחול פערים - התחלה עם פער אחד גדול
    h_gaps = {h: 1}
    v_gaps = {w: 1}
    
    # 3. ערימות (Heaps) למציאת המקסימום במהירות
    # (משתמשים במינוס כי heapq הוא Min-Heap כברירת מחדל)
    h_max_heap = [-h]
    v_max_heap = [-w]
    
    results = []
    
    for i in range(len(isVertical)):
        is_v = isVertical[i]
        dist = distance[i]
        
        # בחירת המערכים הרלוונטיים (אנכי או אופקי)
        lines = v_lines if is_v == 1 else h_lines
        gaps_dict = v_gaps if is_v == 1 else h_gaps
        max_heap = v_max_heap if is_v == 1 else h_max_heap
        
        # אם הקו כבר קיים, אין שינוי
        idx = bisect.bisect_left(lines, dist)
        if idx < len(lines) and lines[idx] == dist:
            # שטח מקסימלי נוכחי
            results.append((-h_max_heap[0]) * (-v_max_heap[0]))
            continue
            
        # מציאת השכנים של הקו החדש כדי לדעת איזה פער נשבר
        prev_line = lines[idx - 1]
        next_line = lines[idx]
        old_gap = next_line - prev_line
        
        # עדכון הקווים
        bisect.insort(lines, dist)
        
        # עדכון הפערים: הסרת הפער הישן והוספת שניים חדשים
        gaps_dict[old_gap] -= 1
        
        new_gap1 = dist - prev_line
        new_gap2 = next_line - dist
        
        for new_gap in [new_gap1, new_gap2]:
            gaps_dict[new_gap] = gaps_dict.get(new_gap, 0) + 1
            heapq.heappush(max_heap, -new_gap)
            
        # ניקוי ה-Heap מערכים שכבר לא קיימים (Lazy Deletion)
        while gaps_dict[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
            
        # חישוב השטח המקסימלי: Max_W * Max_H
        current_max_area = (-h_max_heap[0]) * (-v_max_heap[0])
        results.append(current_max_area)
        
    return results
