class Time:

    """
    Class Time: Allows to tell time, add/sub times,
    add/sub hours, seconds, minutes to time
    :hours, minutes, seconds: list of players who will play dices
    :type hours, minutes, seconds: ints
    (by deafult every arugemnt equals 0)
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.set_time(hours, minutes, seconds)

    def set_time(self, new_hours, new_minutes, new_seconds):
        while True:
            if new_seconds > 59:
                new_seconds -= 60
                new_minutes += 1
            if new_minutes > 59:
                new_minutes -= 60
                new_hours += 1
            if new_minutes < 0:
                new_hours -= 1
                new_minutes += 60
            if new_seconds < 0:
                new_minutes -= 1
                new_seconds += 60
            if new_hours < 0:
                raise ValueError("All inputs must be positive.")
            if (0 <= new_seconds < 59) and (0 <= new_minutes < 59):
                break
        self._hours = int(new_hours)
        self._minutes = int(new_minutes)
        self._seconds = int(new_seconds)

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def __str__(self) -> str:
        return f'{self._hours}:{self._minutes:02}:{self._seconds:02}'

    def __add__(self, other: "Time"):
        new_seconds = self._seconds + other._seconds
        new_minutes = self._minutes + other._minutes
        new_hours = self._hours + other._hours
        return Time(new_hours, new_minutes, new_seconds)

    def __sub__(self, other: "Time"):
        new_seconds = self._seconds - other._seconds
        new_minutes = self._minutes - other._minutes
        new_hours = self._hours - other._hours
        return Time(new_hours, new_minutes, new_seconds)

    def add_hours(self, new_hours):
        self.set_time(self._hours + new_hours, self._minutes, self._seconds)

    def add_minutes(self, new_minutes):
        self.set_time(self._hours, self._minutes + new_minutes, self._seconds)

    def add_seconds(self, new_seconds):
        self.set_time(self._hours, self._minutes, self._seconds + new_seconds)

    def sub_hours(self, new_hours):
        self.set_time(self._hours - new_hours, self._minutes, self._seconds)

    def sub_minutes(self, new_minutes):
        self.set_time(self._hours, self._minutes - new_minutes, self._seconds)

    def sub_seconds(self, new_seconds):
        self.set_time(self._hours, self._minutes, self._seconds - new_seconds)

    def return_seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds
