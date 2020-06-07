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
    def nextDay(dayIdx: int) -> int:
        return (dayIdx + 1) % len(Timestamp.days)

    @staticmethod
    def prevDay(dayIdx: int) -> int:
        return (dayIdx + 6) % len(Timestamp.days)

    @staticmethod
    def normalizeClock(clock: str) -> int:
        clock = clock.strip()
        clock = clock.split(":")
        hour = int(clock[0])
        minutes = int(clock[1])
        return hour * 60 + minutes

    @staticmethod
    def within(subject, start, end) -> bool:
        time_check = True

        if(subject.day == start.day):
            time_check = time_check and subject.time >= start.time

        if(subject.day == end.day):
            time_check = time_check and subject.time <= end.time

        if(start.day <= end.day):
            return subject.day >= start.day and subject.day <= end.day and time_check
        else:
            return subject.day < start.day and subject.day > end.day and time_check

    @staticmethod
    def calculateDuration(source, destination) -> int:
        time = 0
        DAY_COST = 24 * 60  # Number of minutes in one day
        if(source.day < destination.day):
            time = (destination.day - source.day) * DAY_COST
        elif (source.day == destination.day):
            # Case of invalid same day
            if(source.time > destination.time):
                time = 7 * DAY_COST
        else:
            time = (len(Timestamp.days) -
                    (source.day - destination.day)) * DAY_COST
        time = time + destination.time
        time = time - source.time
        return time

    def __str__(self):
        return self.restoreDay(self.day) + " at " + self.restoreClock(self.time)
