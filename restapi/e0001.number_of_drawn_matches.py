import requests
def getNumDraws(year):
    total_draws = 0
    # אנחנו יודעים שקבוצה לא מבקיעה יותר מ-10 שערים לפי האילוצים
    for goals in range(11):
        # בניית ה-URL עם סינון של שערים לכל קבוצה
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={goals}&team2goals={goals}"
        
        response = requests.get(url)
        data = response.json()
        
        # השדה 'total' ב-JSON מחזיר את סך כל המשחקים שעונים על הסינון
        # זה חוסך מאיתנו לעבור דף דף
        total_draws += data['total']
        
    return total_draws



def getNumDraws(year):
    counter = 0
    # פנייה ראשונה כדי לדעת כמה דפים קיימים בסך הכל
    base_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}"
    first_page_response = requests.get(base_url + "&page=1")
    first_page_data = first_page_response.json()
    
    total_pages = first_page_data['total_pages']
    
    # לולאה שעוברת על כל דף ודף (מ-1 עד total_pages כולל)
    for pg in range(1, total_pages + 1):
        response = requests.get(f"{base_url}&page={pg}")
        page_data = response.json()
        
        # מעבר על רשימת המשחקים בתוך הדף הנוכחי
        for match in page_data['data']:
            # המרת השערים למספרים (כי ב-API הם מגיעים כסטרינג)
            if int(match['team1goals']) == int(match['team2goals']):
                counter += 1
                
    return counter