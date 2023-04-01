# Список
nums = [1,3,4,5,6,7,8,2,3,4,5,22222,[2,2,22,2, True, 'Hello']]
nums[0] = 5000
nums[-2] =1.000
print(nums[-1][3])
# Функции списков
numbers = [3,4,5]
b = [4,4,3,5]
numbers.append(100) # добавить один элемент
numbers.insert(1, True) # добавить элемент по индексу
numbers.extend(b) # добавить несколько элементов
numbers.sort() #  сортировка
numbers.reverse() # сортироввка в другую сторону
numbers.pop() # удаление последнего элемента можно о индексу
numbers.remove(4) # удаляет по значению
print(numbers.count(100)) # получить колличество совпадений
print(len(numbers)) # узнать колличество элементов в списке
print(numbers)
#Пример
numeric =[1,3,4,'55', False]
for el in numeric:
    el *=2
    print(el)
# Программа создание списка для пользователя
n = int(input('Ввидите длину списка'))
user_list = []
i = 0
while i < n:
    string = 'Enter element #', str(i +1), ':'
    user_list.append(input(string))
    i +=1
print(user_list)


