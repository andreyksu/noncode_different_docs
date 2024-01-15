# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

speed_p = int(input())
speed_v = int(input())
speed_t = int(input())

max_speed = max(speed_p, speed_v, speed_t)
min_speed = min(speed_p, speed_v, speed_t)

meddle_speed = (speed_p + speed_v + speed_t) - (max_speed + min_speed)

if max_speed == speed_p:
    first_person = "Петя"
elif max_speed == speed_v:
    first_person = "Вася"
else:
    first_person = "Толя"

if meddle_speed == speed_p:
    second_person = "Петя"
elif meddle_speed == speed_v:
    second_person = "Вася"
else:
    second_person = "Толя"

if min_speed == speed_p:
    third_person = "Петя"
elif min_speed == speed_v:
    third_person = "Вася"
else:
    third_person = "Толя"

spaces = " " * 8
print(f"{spaces}{first_person:^8}{spaces}")
print(f"{second_person:^8}{spaces}{spaces}")
print(f"{spaces}{spaces}{third_person:^8}")
print(f"{'II':^8}{'I':^8}{'III':^8}")

'''
Легенды велогонок возвращаются: кто быстрее?
    В новом сезоне за первенство в велогонках вновь борются лучшие из лучших. Протяжённость заключительной трассы — 43872м, и все хотят знать, кто получит золотую медаль.

    Нам известны средние скорости трёх претендентов на победу – Пети, Васи и Толи. Кто из них победит?

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.
    В третьей — Толи.

Формат вывода
    Красивый пьедестал (ширина ступеней 8 символов).

!!!!!Примечание
    В данный момент визуализация тестов работает некорректно.

Ответ на первый тест:

          Петя          
  Толя  
                  Вася  
   II      I      III   
   

Пример 1
Ввод
    10
    5
    7
Вывод
          Петя          
  Толя  
                  Вася  
   II      I      III   
   
   
Пример 2
Ввод
    5
    7
    10
Вывод
          Толя          
  Вася  
                  Петя  
   II      I      III   
'''
