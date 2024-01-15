TheGlovalVar = 4444

class EmployeeSalary():

    hourly_payment = 400
    def __init__(self,  name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @staticmethod
    def get_hourss():
        print(EmployeeSalary.hourly_payment, "staticmethod")

    @classmethod
    def get_hoursss(cls):
        print(cls.hourly_payment, "classmethod")
        
    def get_hourly_payment(self):
        self.hourly_payment = 900000
        return self.hourly_payment
    
    def get_email(cls, name, hours, rest_days):
        email =  f"{cls.name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.get_hours() * self.hourly_payment


ivanov = EmployeeSalary("Ivanov", 8, 3, "ivanov@gmail.com")
ivanov_1 = EmployeeSalary("Ivanov_1", None, 3, "ivanov@gmail.com")
ivanov_2 = EmployeeSalary("Ivanov_2", 8, 3, "")

print(ivanov)
print(ivanov.get_hourly_payment())
print(ivanov.get_hoursss())
#print(ivanov.get_hours("Ivanov_2", 3, "ddd"))