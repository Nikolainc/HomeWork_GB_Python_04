﻿#1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


#data = [x for x in range(1,5)]
#counter = 0
#result = 0
#print(data)

#while counter < len(data):
#    if counter % 2:
#        result += data[counter]
#    counter += 1

#print(f'Сумма чисел на нечетных инедексах: {result}')

#----------------------------------------------------------------

#2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
#И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)


#from random import randint


#Y , X = int(input("Введите количество строк Y: ")), int(input("Введите количество столбцов: "))
#MyArray = [[0] * X for i in range(Y)]

#for i in range(len(MyArray)):
#    for j in range(len(MyArray[i])):
#        MyArray[i][j] = randint(1,9)

#print("Массив создан\n{}".format(MyArray))

#for i in range(len(MyArray)):
#    resultSum = 0
#    for j in range(len(MyArray[i])):
#        resultSum += MyArray[i][j] 
#    resultSum //= len(MyArray[i])
#    print(f"Сумма средне-арифметического строки {i} = {resultSum}")

#----------------------------------------------------------------

#3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

#newArray = [randint(-99,100) for i in range(30)]
#print(newArray)

#for i in range(0, len(newArray)):
#    IndexOfSmalletItem = i
#    for j in range(i + 1, len(newArray)):
#        if newArray[j] < newArray[IndexOfSmalletItem]:
#            IndexOfSmalletItem = j
#    newArray[i], newArray[IndexOfSmalletItem] = newArray[IndexOfSmalletItem], newArray[i]

#print(newArray)