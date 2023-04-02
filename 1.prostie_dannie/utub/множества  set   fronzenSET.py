data = set('hello')
mnogestvo = {4,5,6,7,7,8,6,6,3,4}
mnogestvo.add(7000) # добавить элимент
mnogestvo.update([7000, True,45464]) # добавить несколько чисел
print(mnogestvo.remove(True))# удаление
print(mnogestvo)
# замороженое множество frozenset
new_date = frozenset([5,6,7,7,8,6,6,3,4])
print(new_date)