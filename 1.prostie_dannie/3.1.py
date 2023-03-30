string_sample = "Hello world world "
string_sample_2 = "first letteR is lowEcdease"
string_sample_3 = "extra whivspace"
string_sample_4 = "der FluD"
# определение номера буквы в строке
print(len(string_sample))
print(string_sample[0:5])
print(string_sample[0:12])
print(string_sample[6:11])
print(string_sample[6:11:6])
# проверка строки на присутсвие под строки
print('plane' in string_sample)
#----
print(string_sample_2)
print(type(len('Hello world')))
# преведение в верхний регистр
print(string_sample_2.upper())
# преведение внижний регист
# 1 вариант
print(string_sample_2.lower())
# 2 вариант
print(string_sample_2.casefold())
# делает превый символ большой остальные прописными
print(string_sample_2.capitalize())
#добавление доп символов
print(string_sample_3.strip())
# пример удаление пробелов
user_name = 'anDrei'
print(user_name.capitalize())
print(user_name)
# добавление каких либо элементов в строку
print('Hello',end = '***')
print('world')
# 2 вариант
print(string_sample_3.strip('***'))
# 3 вариант
print(string_sample_3.lstrip())
print(string_sample_3.rstrip())
#заменить что то в строке
print(string_sample.replace('world', 'planet' ))
# примеры
print(string_sample.lower().strip('h').replace('world','planet'))
# потчёт строк в строке  поиск слов
print(string_sample.count('world', 10,17))
print(string_sample.find('world'))