#-*- coding:utf-8 -*-
# Проверяется импорт 'as' т.е. создание коприй.

import sys

from a_pack.a_mod import printOwnAttr
# Создание копий для атрибутов. И они не влияют на исходные атрибуты модуля a_mod
from a_pack.a_mod import inttA as intt
from a_pack.a_mod import strrA as strr
from a_pack.a_mod import listtA as listt
import a_pack.a_mod as a_modd


# Это будут копии и они не повлияют на значение атрибутов модуля a_mod
intt = 1000
strr = "1000"
# listt = list() # Текущая строка закомментирована для проверки listt.append(1000).

# Для изменения их в модуле необходимо воспользоваться именем модуля 
a_modd.intt = 45 # Т.е. без указания объекта модуля мы создаём новую переменную в текущей области.

printOwnAttr()
# Даст
# inttA = 1
# strrA = aaaa
# listtA = [1, 2, 3]

listt.append(1000)
printOwnAttr()

