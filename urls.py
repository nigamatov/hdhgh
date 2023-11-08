# class Student:
#     def __init__(self, name, age, average_grade):
#         self.name = name
#         self.age = age
#         self.average_grade = average_grade
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_average_grade(self):
#         return self.average_grade
#
#     def set_average_grade(self, average_grade):
#         self.average_grade = average_grade
# 
# student1 = Student("Иван", 20, 4.5)
#
#
# name = student1.get_name()
# print("Имя студента:", name)
#
#
# student1.set_name("Петр")
#
#
# age = student1.get_age()
# print("Возраст студента:", age)
#
#
# student1.set_age(21)
#
#
# average_grade = student1.get_average_grade()
# print("Средний балл студента:", average_grade)
#
# student1.set_average_grade(4.8)
#
#
# ##### 2
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_length(self):
#         return self.length
#
#     def set_length(self, length):
#         self.length = length
#
#     def get_width(self):
#         return self.width
#
#     def set_width(self, width):
#         self.width = width
#
#     def calculate_area(self):
#         return self.length * self.width
#
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)
#
#
#
#
#
# rectangle1 = Rectangle(4, 5)
#
#
# area = rectangle1.calculate_area()
# print("Площадь прямоугольника:", area)
#
#
# perimeter = rectangle1.calculate_perimeter()
# print("Периметр прямоугольника:", perimeter)
#
# ##### 3
#
#
# class Car:
#     def __init__(self, make, model, year, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#     def get_make(self):
#         return self.make
#
#     def set_make(self, make):
#         self.make = make
#
#     def get_model(self):
#         return self.model
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_year(self):
#         return self.year
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_mileage(self):
#         return self.mileage
#
#     def set_mileage(self, mileage):
#         self.mileage = mileage
#
#     def display_info(self):
#         print(f"Марка: {self.make}")
#         print(f"Модель: {self.model}")
#         print(f"Год выпуска: {self.year}")
#         print(f"Пробег: {self.mileage} км")
#
#
# car1 = Car("Toyota", "Camry", 2020, 60000)
#
#
# car1.display_info()
#
#
# car1.set_make("Honda")
#
#
# car1.set_mileage(55000)
#
#
# car1.display_info()
#
#
# ##### 4
# class BankAccount:
#     def __init__(self, client_name, balance=0):
#         self.client_name = client_name
#         self.balance = balance
#
#     def get_client_name(self):
#         return self.client_name
#
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         return f"Успешно пополнено. Новый баланс: {self.balance}"
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Недостаточно средств для снятия."
#         else:
#             self.balance -= amount
#             return f"Успешно снято. Новый баланс: {self.balance}"
#
#
# account1 = BankAccount("Нигаматов Руслан")
#
#
# print(account1.deposit(1000))
#
#
# print(account1.withdraw(500))
#
# print(account1.withdraw(1000))
#
#
# print(f"Клиент: {account1.get_client_name()}, Баланс: {account1.get_balance()}")
#


###### 5


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный"
        else:
            return "Разносторонний"

    def calculate_area(self):

        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area



triangle1 = Triangle(5, 7, 10)
print(triangle1.get_triangle_type())
print(triangle1.calculate_area())