
class HourContract:

    def __init__(self, date, value_per_hour, hours):
        self.__date = date
        self.__value_per_hour = value_per_hour
        self.__hours = hours

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = new_date

    @property
    def value_per_hour(self):
        return self.__value_per_hour

    @value_per_hour.setter
    def value_per_hour(self, new_value_per_hour):
        self.__value_per_hour = new_value_per_hour

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, new_hours):
        self.__hours = new_hours

    def total_value(self):
        return self.__hours * self.__value_per_hour
