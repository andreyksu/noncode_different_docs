class Staff:
    map_of_dl = {"Junior": 10, "Middle": 15, "Senior": 20}

    def __init__(self):
        pass

    def getRate(self, a_dl_name):
        return Staff.map_of_dl.get(a_dl_name)

    def nextRate(self, a_dl_name, a_rate):
        listOfDl = list(Staff.map_of_dl.keys())
        if a_dl_name != listOfDl[-1]:
            position = listOfDl.index(a_dl_name)
            a_dl_name = listOfDl[position + 1]
            return Staff.map_of_dl.get(a_dl_name)
        else:
            return a_rate + 1


class Programmer:
    staff = Staff()

    def __init__(self, a_user_name, a_dl_name):
        self.user_name = a_user_name
        self.dl_name = a_dl_name

        self.rate = Programmer.staff.getRate(self.dl_name)

        self.listt_sellary = list()
        self.listt_time = list()

    def work(self, a_time):
        self.listt_time.append(a_time)
        self.listt_sellary.append(a_time * self.rate)

    # Я не знаю как передать текущий рейт (как сейчас, это кастыль).
    # Как сейчас хорошо. Staff - должен хранить информацию о Programmer и его должности и ЗП а не класс Programmer должен хранить информацию эту.
    # При создании нового Programmer он должен регистрироваться в Staff - и Staff уже будет знать всё что нужно о повышении и о текущей должности.
    def rise(self):
        self.rate = Programmer.staff.nextRate(self.dl_name, self.rate)

    def info(self):
        sellary_summ = sum(self.listt_sellary)
        time_summ = sum(self.listt_time)
        return f"{self.user_name} {time_summ}ч. {sellary_summ}тгр."


programmer = Programmer("Васильев Иван", "Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

programmer1 = Programmer("Васильев2 Иван22", "Middle")
programmer1.work(750)
print(programmer1.info())
programmer1.rise()
programmer1.work(500)
print(programmer1.info())
programmer1.rise()
programmer1.work(250)
print(programmer1.info())
programmer1.rise()
programmer1.work(250)
print(programmer1.info())
