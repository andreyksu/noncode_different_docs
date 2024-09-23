"""
Возвращается из класса Генератора 'genClass' из метода '__iter__' новый инстенс итератора iterClass.

Делается возврат нового класса, для возможности множественного прохода по итератору. Это обеспечивается созданием нового инстенса.

Если бы в классе genClass в методе __iter__ возращался self - то можно было бы пройтись только один раз. Т.к. условие в методе __next__ не позволяло бы пройтись еще раз.
Разумеется при условии, что метод __next__ было бы перенсён в класс genClass.
"""
class iterClass:
    def __init__(self, arg):
        self.tmp = 0
        self.arg = arg
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.tmp < self.arg:
            self.tmp = self.tmp + 1.5
            return self.tmp
        else:
            raise StopIteration("Upssss")

class genClass:
    def __init__(self, arg):
        self.arg = arg
    
    def __iter__(self):
        print("Will return new instance of iterClass")
        return iterClass(self.arg)
    

inst = getClass(5)

# Каждый for вызывает метод __iter__ - котолрый получает итератор. А итератор это тот объект, который обладает методом __next__.

for i in inst:
    print(i)
    
for i in inst:
    print(i)