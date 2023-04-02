#data = input('введите текст: ')
#file = open('data/text.txt', 'a')
#file.write(data + '\n')
#file.close()

#Пример
file = open('data/text.txt', 'r')
#print(file.read())
for line in file:
    print(line, end= '')




file.close()