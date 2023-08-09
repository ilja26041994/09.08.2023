# Написать функцию, которая реализует алгоритм "Быстрой сортировки".
# Вводятся следующие параметры:
# - количество значений (с использованием конструкции try-except)
# - ввод чисел с клавиатуры (в список) (с использованием конструкции try-except)

def quick_sort(elem):
    if len(elem) > 1:
        choosen = elem[0]
        left = [i for i in elem if i < choosen]
        right = [i for i in elem if i > choosen]
        return quick_sort(left) + [choosen] + quick_sort(right)
    else:
        return elem
try:
    LenSomeList = int(input('введите количество значений в будущум списке: '))
    someList = input('введите числа через пробел:')
    whisList = someList.split(' ')
    if len(whisList) != len(whisList):
        raise ValueError('invalid input length list input')
except Exception as e:
    print(e)
    print(quick_sort(whisList))