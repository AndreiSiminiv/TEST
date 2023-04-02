#создание функции
def test_func(word):
    print(word, end='')
    print('!')
test_func('hi')

# ПРИМЕР
def summa(a, b ):
    res = a + b
    print('Resul', res)
    return res
res = summa(11.5,45)
res2 = summa('h','i')
print(res, res2)

#ПРиМЕР
nums = [0,5,6,7,99,2,4,]
min = nums[0]
for el in nums:
    if el <min:
        min = el
print(min)
# Замена
def minimal(l):
    min_number = nums[0]
    for el in nums:
        if el < min_number:
            min_number = el
            return min_number
    print(min_number)
min1 = minimal(nums)
# ананимные функции
func = lambda x, y: x*y
res = func(10,23)
print(res)

