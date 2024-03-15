# ОПЕРАТОР IF
# В Python величина отступа имеет значение!!! 

a = 1
b = 1
if a < b : 
    print("a < b")
elif a < b : 
    print("b > a")
else : 
    print("b = a")
# Отличие от JAVA: 
# блок операторов if не заключается в скобки, достаточно двоеточия и отступа. 

if a != b : 
    print(f"{min(a,b)} меньше, чем {max(a,b)}") 
else: 
    print(f"{a} равно {b}") 

# КАЛЬКУЛЯТОР ИНДЕКСА МАССЫ ТЕЛА: 
    
name = "Tom"
weight = 72
height = 1.68

bmi = weight / (height**2)
print("Индекс массы тела человека с именем {} равен {}".format(name, bmi))
if bmi <= 24.9 and bmi >= 18.5 : 
    print("Это нормальный вес")
elif bmi < 18.5 :
    print("Это - истощение") 
else : 
    if bmi > 30 : 
        print("Это - ожирение")
    else : 
        print("Это избыточный вес")
    

