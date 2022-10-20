from datetime import datetime

class Order:

    def __init__(self):
        self.__moment = datetime.now()
        self.__items = []

    def get_moment(self):
        return '{}/{}/{} {}:{}'.format(self.__moment.day, self.__moment.month, self.__moment.year, self.__moment.hour, self.__moment.minute)

    def get_items(self):
        return self.__items

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def total(self):
        sum = 0
        for item in self.__items:
            sum += item.sub_total()
        return sum
