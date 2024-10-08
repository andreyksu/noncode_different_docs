# Сделал через стек - но не правильно не в соответстии с алгоритмом который предлагается для Польской обратной записи.
# А не нравится потому что сделано не правильно.

inputed_str = input()

listt_as_stack = inputed_str.split()

# !!!!!! Раз не нравится. Потребность в перестановке элементов. А если длинный список????
listt_as_stack.reverse()
fuzze = True
operation_list = ["*", "**", "/", "%", "//", "-", "+"]
# Два не нравится. Потребность в еще одном списке. Но он по сути создаётся один раз.
second_list = list()
while fuzze:
    extracted_element = listt_as_stack.pop()
    if extracted_element not in operation_list:
        second_list.append(int(extracted_element))
    else:
        result = 0
        second = int(second_list.pop())
        first = int(second_list.pop())
        oper = extracted_element

        if oper == "*":
            result = first * second
        elif oper == "**":
            result = first**second
        elif oper == "/":
            result = first / second
        elif oper == "%":
            result = first % second
        elif oper == "//":
            result = first // second
        elif oper == "-":
            result = first - second
        elif oper == "+":
            result = first + second

        listt_as_stack.append(result)
        # !!!!!! Три не нравится. Снова перестановка во вспомогательном списке. Можно конечно в цикле обратно переложить. Но тоже вариант так себе.
        second_list.reverse()
        # Четыре на нравится. Но это и в первом решении было, видимо никуда не деться от этого.
        listt_as_stack = listt_as_stack + second_list
        second_list.clear()
        if len(listt_as_stack) == 1:
            fuzze = False

print(listt_as_stack[0])


"""
Польский калькулятор

Напишите программу, которая производит вычисление выражения, записанного в обратной польской нотации (ОПН).

В ОПН нет ни скобок, ни приоритета операторов («умножение раньше сложения»).

Чтобы прочитать выражение, записанное в таком формате, нужно просматривать выражение строго последовательно. Вводимые значения последовательно добавляются в стек. Когда встречается символ операции, то из стека извлекаются последние положенные туда значения, с ними проделывается эта операция и результат возвращается в стек.

Если для операции важен порядок значений, с которыми она производится, то первым идёт число, лежавшее в стеке глубже. В частности, если операция — вычитание, то из предпоследнего числа в стеке вычитается последнее, а не наоборот.

Изначально стек пустой, в результате полного вычисления выражения в нём должно остаться одно значение — результат вычислений.

Первый пример следует читать так: в стек последовательно добавляются значения 7 2 3, а затем встречаем знак операции *. Тогда значения 2 и 3 извлекаются, перемножаются, результат 6 кладётся обратно в стек. Следующий знак извлекает из стека два оставшихся в нём значения 7 и 6, вычитает одно из другого и кладёт результат снова в стек. Выражение закончилось, в стеке одно число — 1, это и есть результат вычисления.
Формат ввода

Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций +, -, *, которые вместе составляют корректное выражение в обратной польской нотации.
Формат вывода

Выводится одно целое число — результат вычисления выражения.
Пример 1
Ввод
7 2 3 * -
Вывод
1

Пример 2
Ввод
10 15 - 7 *
Вывод
-35

"""
