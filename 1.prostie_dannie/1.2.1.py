side_A = float(input('Enter side A : '))
side_B = float(input('Enter side B : '))
side_C = float(input('Enter side C : '))

half_perimetr = (side_A + side_B + side_C)/2
trengele_area = half_perimetr * (half_perimetr - side_A) * (half_perimetr - side_B)*(half_perimetr-side_C) ** 0.5

print('side A = ' + str(side_A) )
print('side B = ' + str(side_B) )
print('side C = ' + str(side_C) )
print('Area of trengele is ' + str(trengele_area))

area = input( "pleas :")
print(float(input( "pleas :")))
print(area)
print('Area = ')