class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_format_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{Clock.__get_formatted_num(h)}:{Clock.__get_formatted_num(m)}:{Clock.__get_formatted_num(s)}"

    @staticmethod
    def __get_formatted_num(num):
        return str(num) if num > 9 else f"0{num}"

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Операнд должен быть типом Clock")
        return Clock(self.seconds + other.seconds)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(" операнд должен быть типом Clock")
        return self.seconds == other.seconds

    def __ne__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(" операнд должен быть типом Clock")
        return self.seconds != other.seconds

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return Clock((self.seconds - other.seconds) % self.__DAY)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return Clock((self.seconds * other.seconds) % self.__DAY)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return Clock((self.seconds // other.seconds) % self.__DAY)

    def __mod__(self, other: 'Clock') -> 'Clock':
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return Clock((self.seconds % other.seconds) % self.__DAY)

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(" операнд должен быть типом Clock")
        self.seconds += other.seconds
        self.seconds %= self.__DAY
        return self

    def __isub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(" операнд должен быть типом Clock")
        self.seconds -= other.seconds
        self.seconds %= self.__DAY
        return self

    def __imul__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        self.seconds *= other.seconds
        self.seconds %= self.__DAY
        return self

    def __ifloordiv__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        self.seconds //= other.seconds
        self.seconds %= self.__DAY
        return self

    def __imod__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        self.seconds %= other.seconds
        self.seconds %= self.__DAY
        return self

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return self.seconds < other.seconds

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return self.seconds <= other.seconds

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return self.seconds > other.seconds

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise TypeError(" операнд должен быть типом Clock")
        return self.seconds >= other.seconds


c1 = Clock(100)
c2 = Clock(200)
print(c1.get_format_time())
print(c2.get_format_time())

# Результаты операций
print("Сложение:", (c1 + c2).get_format_time())
print("Вычитание:", (c1 - c2).get_format_time())
print("Умножение:", (c1 * c2).get_format_time())
print("Целочисленное деление:", (c1 // c2).get_format_time())
print("Остаток от деления:", (c1 % c2).get_format_time())

# Изменение текущего объекта
c1 += c2
print("Изменение текущего объекта (сложение):", c1.get_format_time())
c1 -= c2
print("Изменение текущего объекта (вычитание):", c1.get_format_time())
c1 *= c2
print("Изменение текущего объекта (умножение):", c1.get_format_time())
c1 //= c2
print("Изменение текущего объекта (целочисленное деление):", c1.get_format_time())
c1 %= c2
print("Изменение текущего объекта (остаток от деления):", c1.get_format_time())

# Сравнение
if c1 < c2:
    print("Первое время меньше второго")
elif c1 <= c2:
    print("Первое время меньше или равно второму")
elif c1 > c2:
    print("Первое время больше второго")
elif c1 >= c2:
    print("Первое время больше или равно второму")
