def reverse_words_order_and_swap_cases(sentence):
    # 1. החלפת מצב האותיות (Lower -> Upper, Upper -> Lower)
    swapped_case = sentence.swapcase()
    
    # 2. פיצול המשפט לרשימת מילים לפי רווחים
    words = swapped_case.split(' ')
    
    # 3. היפוך סדר המילים ברשימה
    reversed_words = words[::-1]
    
    # 4. חיבור המילים בחזרה למחרוזת אחת עם רווחים ביניהן
    return ' '.join(reversed_words)

# בדיקה עם הדוגמה מ-image_8cfa5a.png
input_str = "aWESOME is cODING"
print(reverse_words_order_and_swap_cases(input_str))
# פלט מצופה: Coding IS Awesome



#longer
def reverse_words_order_and_swap_cases(sentence):
    # פיצול המשפט למילים
    words = sentence.split(' ')
    
    # מימוש ידני של היפוך רשימה (Two Pointers)
    left = 0
    right = len(words) - 1
    
    while left < right:
        # החלפת ערכים (Swap)
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
        
    # כעת words הפוכה. נחבר אותה ונטפל ב-Case
    reversed_sentence = ' '.join(words)
    
    # החלפת Case ידנית (כפי שראינו קודם)
    result = ""
    for char in reversed_sentence:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
            
    return result