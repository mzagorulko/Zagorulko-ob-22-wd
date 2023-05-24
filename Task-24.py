class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print(f"Cотрудник по имени {self.name}, {self.age} лет, и зарплата - {self.salary} рублей.")


employee = Employee("Михаил", 33, 200000)
employee.info()
