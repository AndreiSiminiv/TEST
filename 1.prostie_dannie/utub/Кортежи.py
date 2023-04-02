# используются для передачи данных Tuple изменять не льзя
data = ('football','basketball','skate',1.2, 45, True)
print(data[1:5])
print(data.count(45))
print(len(data))
print(data)
# пример
data = ('football','basketball','skate',1.2, 45, True)
for i in data:
    print(i)
# преоброзовать список в кортедж
nums = [1,3,5,5,6]
new_date = tuple(nums)
print(new_date)