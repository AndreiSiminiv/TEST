country ={'code':'RU', 'name': 'Russion', 'populetion': 144 }
print(country['name'])
# пример с dict
strana = dict(code= 'Ru', name='Russian')
print(strana)
for key, val in strana.items():
    print(key,'-', val)
# функции словарей
spb ={'code':'RU', 'name': 'Russion', 'populetion': 144 }
print(spb.get('name'))
print(spb.pop('code'))# удалить  один элемент
print(spb.keys()) # получить спичок ключей
print(spb.values())# получить значения
print(spb.items()) # получить значение и код
spb['name']= 'None' # переминовать
# пример использование словаря
person ={
    'user_1': {
        'first_name': 'Jon',
        'last_name': 'Marli',
        'age': 45,
        'adres': ['г.Москва', 'ул.Долгоозерная', '45'],
        'grandes':{'math': 5, 'fiz': 4 }
    },
}
print(person['user_1']['adres'][1])