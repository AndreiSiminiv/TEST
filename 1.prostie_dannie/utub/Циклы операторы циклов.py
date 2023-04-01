# цикл FOR
#for i in range(1, 6, 2):
#    print(i)

#пример поиск определенного символа в строке
#count =0
#world = 'Heloo world'
#for i in world:
#    if i =='w':
#        count+=1
#print("Count", count)

# цикл while
#i = 5
#while i <= 15:
 #   print(i)
  #  i +=2

#isHasCar = True
#while isHasCar:
  #  if input() =="Stop":
   #     isHasCar = False

#Операторы используемые в циклах
#for i in range(1, 11):
 #   if i == 5:
  #      break
   # if i % 2 ==0:
    #    continue
   # print(i)

#программа для нахождения символов в строке
found = None
for i in 'hello':
    if i == 'j':
        found = True
        break
else:
    found = False
print(found)