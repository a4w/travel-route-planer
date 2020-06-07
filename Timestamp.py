class Timestamp:
    days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

    def __init__(self, day: str, time: str):
        self.day = self.normalizeDay(day)
        self.time = self.normalizeClock(time)

    @staticmethod
    def normalizeDay(day: str) -> int:
        day = day.strip().lower()
        return Timestamp.days.index(day)

    @staticmethod
    def restoreDay(dayIdx: int) -> str:
        return Timestamp.days[dayIdx]

    @staticmethod
    def restoreClock(time: int) -> str:
        hour = time // 60
        minute = time % 60
        return ("0" + str(hour))[-2:] + ":" + ("0" + str(minute))[-2:]

    @staticmethod
    def nextDay(dayIdx: int):
        return (dayIdx + 1) % len(Timestamp.days)

    @staticmethod
    def normalizeClock(clock: str) -> int:
        clock = clock.strip()
        clock = clock.split(":")
        hour = int(clock[0])
        minutes = int(clock[1])
        return hour * 60 + minutes

    def __str__(self):
        return self.restoreDay(self.day) + " at " + self.restoreClock(self.time)

