class Employee:
    emp_count = 0
    work_rate = 2
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_count(self):
        pass
    def display_employee(self):
        print("Мое имя ", self.name)
        print("Зарплаата ", self.salary)

    def change_name(self,new_name):
        self.name = new_name

    def get_total_salary(self):
        return self.salary

