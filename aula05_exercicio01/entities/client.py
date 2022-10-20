
import email
from tkinter import N
from unicodedata import name


class Client:

    def __init__(self, name, email, birth_date) -> None:
        self.__name = name
        self.__email = email
        self.__birth_date = birth_date

    def __str__(self):
        return f'Client: {self.__name}' + ' (' '{}/{}/{}'.format(self.__birth_date.day, self.__birth_date.month, self.__birth_date.year) + ') - ' + f'{self.__email}'