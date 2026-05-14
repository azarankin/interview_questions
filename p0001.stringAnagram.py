#O(n L log L + q L log L).
#space O(n L + q)
def stringAnagram(dictionary, query):
    # נשתמש במילון כדי לספור מופעים של מילים מנורמלות
    counts = {}
    
    for word in dictionary:
        # נרמול: מיון האותיות יוצר מפתח זהה לכל האנאגרמות
        sorted_word = "".join(sorted(word))
        counts[sorted_word] = counts.get(sorted_word, 0) + 1
        
    results = []
    for q in query:
        # נרמול השאילתה ובדיקה במפת הזיכרון
        sorted_q = "".join(sorted(q))
        results.append(counts.get(sorted_q, 0))
        
    return results