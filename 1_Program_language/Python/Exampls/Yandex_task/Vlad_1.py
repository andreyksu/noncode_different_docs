class EmployeeSalary:
    
    # hourly_payment = 400 # Делаем статическим полем(если есть требование чтоб они было статическим).
    # Но так лучше не делать. Ибо все будут получать одну ЗП.
    
    def __init__(self, aName, aHours, aRest_days, aEmail):
        self.name = aName
        self.hours = aHours
        self.rest_days = aRest_days
        self.email = aEmail
        
        self.hourly_payment = 400 # <<<<<< Лучше так.
    
    def get_hours(self):
        if not self.hours:
            return (7 - self.rest_days) * 8
        return self.hours
    
    def get_email(self):
        if not self.email:
            return f"{self.name}@email.com"
        return self.email

    def set_hourly_payment(self, aHourly_payment):
        self.hourly_payment =  aHourly_payment
        
    def salary(self):
        return self.get_hours() * self.hourly_payment
    
    
worker_1 = EmployeeSalary("Fedor", 30, 3, "mailFedor@gmail.com")
print(worker_1.get_email(), worker_1.get_hours(), worker_1.salary())
worker_1.set_hourly_payment(200)
print(worker_1.get_email(), worker_1.get_hours(), worker_1.salary())
worker_1.set_hourly_payment(1000)
print(worker_1.get_email(), worker_1.get_hours(), worker_1.salary())


worker_2 = EmployeeSalary("Egor", None, 1, "")
print(worker_2.get_email(), worker_2.get_hours(), worker_2.salary())
worker_2.set_hourly_payment(10000)
print(worker_2.get_email(), worker_2.get_hours(), worker_2.salary())