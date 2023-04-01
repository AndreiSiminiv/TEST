# с трайными кавычками можно делать преносы
a= 'cascac'
b = ""
c= """машина
hello
world
planet
"""
d= 1234
print(c)
print(a, b,d, c )
# состовление строк {}
salary=1000
user_name = 'Jon'
string_new = '{1}Jons salary is {0}'
print(string_new.format(salary,user_name))
#Более удобный способ для разработчиков
new_string = 'This {product} costs {price:.2f} evros'
print(new_string.format(product='computer', price = 1000))
# устаревший но испльзуется
x =215121.242
y=353653.53
print('The valeu x is %.f'%x)
print('The valeu x is %.4f'%y)
# Самый удобный способ
name = 'Andrey'
fest_name = 'Simonov'
yeur = 36
print(f'Hi {name} {fest_name} {yeur-20}  smail')
# произвести кодировку строки часто используется utf-16'
name_string = "Jonn Vikk"
name_string = name_string.encode('utf-16')
print(name_string)
# раскодировать строку
print(name_string.decode('utf-16'))

# if elif else
x = 6

if x <10:
      print('x smaller than 10')
elif x ==5:
    print('x is equal 5')
else:
    print('Nothing happened')
print('FINISH')
#------------------------------
id_code = input('Please enter id: ')
if len(id_code) == 11:
    print('Your id code is' + id_code)
elif len(id_code) >11:
    print('Your code is too long')
else:
    print('Your code is too short')
