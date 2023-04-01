# как записать все в один ряд end=
print('Hello world', sep='|',end='')
print('Результат:',2,4,6,78, sep='|', end='')
print('Second line\'L\ni\n\ne')
#  сложение в принт
print('Результат:', 100 +1000)
print(min(1,2,4,6,77,7,5,33,3))
print(max(45,6,7,4,5,4,3))
print(abs(-5))
print(pow(55, 3))
print(round(5/3))
# получение данных от пользователя
#input('введите свой возвраст: ')
#переменные
number = 5 #int
print("Результат:", number)
number = 7
print("Результат:", number)
# десятичные цифры
digit = 4.55446464 #float
word = 'Результат:' #string
print(word, digit)
# буливые
boolean = True #boolean
print(boolean)
# переделать тип данных
print(word + str(digit))
str_num = "5"
print(word + str(int(str_num) + number))
# пример небольшая программка
num1 = int(input('Введите первое число:  '))
num2 = int(input('Введите второе число:  '))

num1+=5

print('Результат : ', num1 + num2)
print('Результат : ', num1 - num2)
print('Результат : ', num1 / num2)
print('Результат : ', num1 * num2)
print('Результат : ', num1 ** num2)
print('Результат : ', num1 // num2)

word = 'hi'
print(word *2)