class RaptorDateTime:
    MINUTES_PER_HOUR = 60
    SECONDS_PER_MINUTE = 60
    HOURS_PER_DAY = 24
    MONTH_PER_YEAR = 12
    DAYS_PER_YEAR = 365
    DAYS_PER_MONTH: dict[int, int] = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31, 
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def validate(self) -> None:
        def _validate_year() -> None:
            pass

        def _validate_month() -> None:
            if self.month > self.MONTH_PER_YEAR or self.month <= 0:
                raise ValueError("В году только 12 месяцев!")
            
        def _validate_day() -> None:
            if self.day <= 0:
                raise ValueError("Дни не могут быть отрицательны!")
            if self.day > self.DAYS_PER_MONTH[self.month]:
                raise ValueError(f"В данном месяце меньше дней, чем {self.day}!")
        
        def _validate_hour() -> None:
            if self.hour > self.HOURS_PER_DAY or self.hour < 0:
                raise ValueError("Время в формате 24 часов!")
            
        def _validate_minute() -> None:
            if self.minute > self.MINUTES_PER_HOUR or self.minute < 0:
                raise ValueError("В часе только 60 минут!")
        
        def _validate_second() -> None:
            if self.second > self.SECONDS_PER_MINUTE or self.second < 0:
                raise ValueError("В минуте только 60 секунд!")
        
        _validate_year()
        _validate_month()
        _validate_day()
        _validate_hour()
        _validate_minute()
        _validate_second()

    def __str__(self) -> str:
        return (
            f"Year: {self.year}. "
            f"Month: {self.month}. "
            f"Day: {self.day}. "
            f"Hour: {self.hour}. "
            f"Minute: {self.minute}. "
            f"Second: {self.second}."
        )
    
    @property
    def days(self) -> int:
        days = self.day + self.year * self.DAYS_PER_YEAR
        return days
    
    def __init__(
        self, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0
    ) -> None:
        self.year = year 
        self.month = month 
        self.day = day 
        self.hour = hour 
        self.minute = minute 
        self.second = second
        self.validate()

    def __sub__(self, other_date: "RaptorDateTime") -> int:
        if type(other_date) != self.__class__:
            raise ValueError(
                f"RaptorDateTime нельзя применить операцию '-' в типом данных  {type(other_date)}"
            )
        new_hour = self.hour - other_date.hour
        new_minute = self.minute - other_date.minute
        new_second = self.second - other_date.second
        if new_second < 0:
            new_minute -= 1
            new_second = self.SECONDS_PER_MINUTE + new_second
        if new_minute < 0:
            new_hour -= 1
            new_minute = self.MINUTES_PER_HOUR + new_minute
        if new_hour < 0:
            other_date.day += 1
            new_hour = self.HOURS_PER_DAY + new_hour
        seconds = (
            new_second + new_minute * self.SECONDS_PER_MINUTE + new_hour * self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR
        )
        
        return self.days - other_date.days, seconds
    

a = RaptorDateTime(year=2000, month=10, day=4, hour=20, minute=5, second=5)
b = RaptorDateTime(year=2000, month=10, day=3, hour=20, minute=10, second=5)
print(a - b)


# Я так понимаю задача ориентировалась на это
# https://www.geeksforgeeks.org/python-program-to-find-number-of-days-between-two-given-dates/
# Я сделал свой вариант