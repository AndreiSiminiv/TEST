word = 'football, basketball, skate'
print(word[1]) # вывести необходимый сивол
print(len(word)) # вывести количество символов
print(word.count('p')) # вывести сколько похожих символов существует
print(word.upper()) # привести вверхний регистр
print(word.isupper()) # проверка регистра
print(word.lower()) # к нижнему регистру
print(word.find('p'))# поиск определенных символов в строке
#---
hobby = word.split(', ')
print(hobby[0])# разбить строку по определенному символу
#---
# Напишем программу обращаться к каждому элементу списка
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
result  = ', '.join(hobby)
print(result)


# индекс и срезы
word = 'football'
print(word[4:-1]) # вывести несколько элементов
print(word[1:-1:2]) # указать шаг
# пример на списке
lis = [1,4,6,6.6, 'stroka', True]
print(lis[2:-3:2])
# сортировка
print(lis[::2])