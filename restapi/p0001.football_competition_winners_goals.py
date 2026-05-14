import requests

def getWinnerTotalGoals(competition, year):
    # --- שלב 1: מציאת הקבוצה המנצחת ---
    comp_url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}"
    response = requests.get(comp_url).json()
    
    # בדרך כלל יש רק תוצאה אחת במערך ה-data
    winner_team = response['data'][0]['winner']
    
    # --- שלב 2: סכימת גולים ---
    total_goals = 0
    
    # פונקציית עזר לסכימת גולים ב-endpoint של המשחקים
    # אנחנו צריכים לבדוק פעמיים: פעם אחת כשהקבוצה מארחת ופעם כשאורחת
    for team_role in ['team1', 'team2']:
        page = 1
        while True:
            match_url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&{team_role}={winner_team}&page={page}"
            match_data = requests.get(match_url).json()
            
            for match in match_data['data']:
                # אם חיפשנו אותה כ-team1, ניקח את team1goals
                total_goals += int(match[f'{team_role}goals'])
            
            # בדיקה אם יש עוד דפים
            if page >= match_data['total_pages']:
                break
            page += 1
            
    return total_goals