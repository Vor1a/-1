import doctest


class Employee:
    empCount = 0

    def __init__(self, name: str, salary: float):
        if not isinstance(name, str):
            raise TypeError("Имя сотрудника должно быть типа str")
        self.name = name
        if not isinstance(salary, float):
            raise TypeError("Зарплата сотрудника должна быть типа float")
        self.salary = salary
        Employee.empCount += 1

        """
        emp1 = Employee("Dmitry", 100000.123)
        """

    def salary_up(self, salary_add):
        """
        Функция повышает зарплату сотрудника
        emp1 = Employee("Dmitry", 100000.345)
        emp1.salary_up(5000)

        if not isinstance(salary_add, float):
            raise TypeError("Добавляемая сумма должна быть типа float")
        if salary_add < 0:
            raise ValueError("Добавляемая сумма должна положительным числом")
        """

    def displayEmployee(self):
        """
        Функция выводит на экран информацию о сотруднике.
        emp1 = Employee("Dmitry", 100000.345)
        emp1.displayEmployee()
        """


class Pet:
    def __init__(self, name, happiness=0):
        if not isinstance(name, str):
            raise TypeError("Имя питомца должно быть типа str")
        self.happiness = happiness
        self.name = name
        """
        pet1 = Pet("Juja")
        """

    def play(self):
        """
        Функция позволяет поиграть с питомцем и выводит текущий уровень счастья.
        pet1 = Pet("Juja")
        pet1.play()
        """

    def feed(self):
        """
        Фунцкия позволяет покормить питомца и выводит текущий уровень счастья.
        pet1 = Pet("Juja")
        pet1.feed()
        """


class Bed:
    def __init__(self, status, sheets):
        self.status = status
        self.sheets = sheets
        """
        bed1 = Bed()
        """
    def change_status(self):
        """
        Фукнция меняет статус кровати с "заправленной" на "разобранную" и показывает текущие данные кровати.
        bed1 = Bed()
        bed1.change_status()
        """
    def change_sheets(self):
        """
        Функция обновляет постельное белье и показывает текущие данные кровати.
        bed1 = Bed()
        bed1.change_sheets()
        """


if __name__ == "__main__":
    doctest.testmod()
