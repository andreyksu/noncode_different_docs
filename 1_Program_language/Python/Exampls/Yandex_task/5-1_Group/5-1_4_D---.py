map_of_dl = {"Junior": 10, "Middle": 15, "Senior": 20}  # Переделать на класс.


class Programmer:
    def __init__(self, a_user_name, a_dl_name):
        self.user_name = a_user_name
        self.dl_name = a_dl_name

        self.rate = map_of_dl.get(self.dl_name)

        self.listt_sellary = list()
        self.listt_time = list()

    def work(self, a_time):
        self.listt_time.append(a_time)
        self.listt_sellary.append(a_time * self.rate)

    def rise(self):
        listOfDl = list(
            map_of_dl.keys()
        )  # Эта реализация должа быть в классе map_of_dl - т.к. класс map_of_dl должен описывать и содержать в себе и должности и правила повышения. И должен быть метод next()
        if self.dl_name != listOfDl[-1]:
            position = listOfDl.index(self.dl_name)
            self.dl_name = listOfDl[position + 1]
            self.rate = map_of_dl.get(self.dl_name)
        else:
            self.rate += 1

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


"""
Работа не волк
Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов. Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании существуют 3 должности:

Junior — с окладом 10 тугриков в час;
Middle — с окладом 15 тугриков в час;
Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). Класс реализует следующие методы:

work(time) — отмечает новую отработку в количестве часов time;
rise() — повышает программиста;
info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример
Ввод
    programmer = Programmer('Васильев Иван', 'Junior')
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
Вывод
    Васильев Иван 750ч. 7500тгр.
    Васильев Иван 1250ч. 15000тгр.
    Васильев Иван 1500ч. 20000тгр.
    Васильев Иван 1750ч. 25250тгр.

"""