

class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email=None):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_rate):
        cls.hourly_payment = new_rate

    def salary(self):
        return self.hours * self.hourly_payment
    

emp1 = EmployeeSalary.get_hours("Лиза Кучкова", rest_days=4)
print(emp1.salary())  


emp2 = EmployeeSalary.get_email("Максим Максимов")
print(emp2.email)
emp2 = EmployeeSalary.get_hours("Kfyf Kfyjdf", rest_days=3)
  

EmployeeSalary.set_hourly_payment(800)
print(emp1.salary()) 

EmployeeSalary.set_hourly_payment(1800)
print(emp2.salary()) 