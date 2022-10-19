
class Client:

    def __init__(self, name, email, birth_date):
        self.__name = name
        self.__email = email
        self.__birth_date = birth_date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, new_birth_date):
        self.__birth_date = new_birth_date

    def __str__(self):
        birth_date_fmt = '{}/{}/{}'.format(self.__birth_date.day, self.__birth_date.month, self.__birth_date.year)
        return f'{self.__name} ({birth_date_fmt}) - {self.__email}'
