def hours_hand(hour, minutes):
    base = (hour % 12 ) * (360 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction

def minutes_hand(hour, minutes):
    return minutes * (360 // 60)

def between(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(hour, minutes))
