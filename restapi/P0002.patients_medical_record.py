import requests

def getAverageTemperatureForUser(userId):
    url = f"https://jsonmock.hackerrank.com/api/medical_records?userId={userId}"
    
    # קריאה ראשונה כדי לקבל את מספר הדפים הכולל
    response = requests.get(url + "&page=1").json()
    total_pages = response['total_pages']
    
    all_temperatures = []
    
    # לולאה על כל הדפים (כולל הראשון שכבר קראנו, או להתחיל מ-1 עד total_pages + 1)
    for page in range(1, total_pages + 1):
        page_data = requests.get(f"{url}&page={page}").json()
        
        for record in page_data['data']:
            temp = record['vitals']['bodyTemperature']
            all_temperatures.append(temp)
            
    # טיפול במקרה שאין נתונים
    if not all_temperatures:
        return "0"
        
    # חישוב ממוצע
    avg = sum(all_temperatures) / len(all_temperatures)
    
    # החזרה כסטרינג עם ספרה אחת אחרי הנקודה
    return format(avg, ".1f") #return str(round(avg, 1)) #return "{:.1f}".format(avg)