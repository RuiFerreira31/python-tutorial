class Time:
    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = h

    # Read-only field accessors
    @property
    def hours(self):
        return self._h

    @property
    def minutes(self):
        return self._m

    @property
    def seconds(self):
        return self._s

    def _cmp(time1, time2):
        if time1._h < time2._h:
            return 1
        if time1._h > time2._h:
            return -1
        if time1._m < time2._m:
            return 1
        if time1._m > time2._m:
            return -1
        if time1._s < time2._s:
            return 1
        if time1._s > time2._s:
            return -1
        return 0

    def __eq__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self._h == other._h and self._m == other._m and self._s == other._s

    def __lt__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        if self._h != other._h:
            return self._h < other._h
        if self._m != other._m:
            return self._m < other._m
        return self._s < other._s

    def __le__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        if self._h != other._h:
            return self._h < other._h
        if self._m != other._m:
            return self._m < other._m
        if self._s == other._s:
            return self._s == other._s
        return self._s < other._s


t1 = Time(13, 10, 5)
t2 = Time(5, 15, 30)
t3 = Time(5, 15, 30)
print(t1 < t2)
print(t1 > t2)
print(t1 == t2)
print(t2 == t3)