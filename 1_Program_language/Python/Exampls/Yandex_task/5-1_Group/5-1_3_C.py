class RedButton:
    def __init__(self):
        self.countt = 0

    def click(self):
        self.countt += 1
        print("Тревога!")

    def count(self):
        return self.countt
    
first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())