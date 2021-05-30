class Test:
    def hours_hand(self, hour, minutes):
        base = (hour % 12 ) * (360 // 12)
        correction = int((minutes / 60) * (360 // 12))
        return base + correction

    def minutes_hand(self, hour, minutes):
        return minutes * (360 // 60)

    def between(self, hour, minutes):
        return abs(self.hours_hand(hour, minutes) - self.minutes_hand(hour, minutes))
