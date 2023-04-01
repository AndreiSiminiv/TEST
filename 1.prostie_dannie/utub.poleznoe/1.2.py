int_var =500
float_var =50.5
string_var_text ='Hello world'
string_var_num ='134.4'
bull_var = True

print(string_var_text+str(int_var))
print(int_var)

int_var = str(int_var)
print(int_var)
print(string_var_text + str(bull_var))

print(int_var)
print(float(int_var))
print(int(float_var))

print(type(float(string_var_num)))

print(bool(int_var))
print(int_var,string_var_num,string_var_text, bull_var,10000)

print(float_var + float(string_var_num))
print(float_var) + (string_var_num)

