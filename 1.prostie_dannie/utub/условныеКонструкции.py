user_data = int(input('Введите число: '))

isHappy = True

if isHappy and user_data:
    print("Пользователь доволен")
elif user_data ==5:
    print("Номер 5 ")
else:
    print('Пользователь не доволен')

if isHappy or user_data:
    print("Пользователь доволен")
elif user_data ==5:
    print("Номер 5 ")
else:
    print('Пользователь не доволен')

if user_data != 5:
    print('мы на месте')
    if user_data > 6:
        print('Namber is bigger than 5')