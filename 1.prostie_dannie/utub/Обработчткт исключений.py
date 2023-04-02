try:
    x =  int(input('введите число: '))
    x +=5
    print(x)
except ValueError:
    print('Введите число лучше ')

#Небольшая программа
x = 0
while x == 0:
    try:
        x = int(input('введите число: '))
        x += 5
        print(x)
    except ValueError:
        print('Введите число лучше ')

# отслеживание ошибок
try:
    x=5/0
except  ZeroDivisionError:
    print('Деление не возможно')
except ValueError:
    print('Смотрите внемательней')
else:
    print('else')
finally:
    print('Спасибо')