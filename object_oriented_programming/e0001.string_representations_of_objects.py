#oop

class Car:
    def __init__(self, max_speed, unit):
        # הקונסטרוקטור מקבל מהירות מקסימלית ויחידות מידה
        self.max_speed = max_speed
        self.unit = unit

    def __str__(self):
        # מחזיר את המחרוזת בפורמט הנדרש: "Car with the maximum speed of X Y"
        return f"Car with the maximum speed of {self.max_speed} {self.unit}"

class Boat:
    def __init__(self, max_speed):
        # הקונסטרוקטור מקבל מהירות מקסימלית בקשרים (knots)
        self.max_speed = max_speed

    def __str__(self):
        # מחזיר את המחרוזת בפורמט הנדרש: "Boat with the maximum speed of X knots"
        return f"Boat with the maximum speed of {self.max_speed} knots"


# זה הקוד שרץ ברקע ולא צילמת, אבל ככה הוא משתמש בפתרון שלך:
q = int(input()) # מספר השאילתות
for _ in range(q):
    line = input().split()
    vehicle_type = line[0]
    
    if vehicle_type == "car":
        max_speed = int(line[1])
        unit = line[2]
        obj = Car(max_speed, unit)
    elif vehicle_type == "boat":
        max_speed = int(line[1])
        obj = Boat(max_speed)
    
    print(obj) # כאן מופעל ה-__str__ שכתבת!