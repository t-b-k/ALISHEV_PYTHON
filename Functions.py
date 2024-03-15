# Функция - это некоторый именованый блок кода

def function1() : 
    # Все, что внутри, должно идти с отступом
    # Один стандартный отступ в Python равен 4 пробелам
    print("Это сработала функция function1")

# Возврат к нулевому отступу означает, что вы уже за пределами кода функции
print("Это код, который описан в теле программы за пределами определения функции")

# Вызов функции выглядит так: 
function1()

def function2 (x) : 
    return 2*x

a = 4
ax2 = function2(a)
print(f"2 * {a} = {ax2}")

# Если функция не возвращает никакого значения, а мы присвоим результат ее работы некоторой переменной, 
# то значение этой переменной будет равняться None : 

def function3 () : 
    pass

a = function3()
print(a)

def function4(x) : 
    print(x)
    print("Работает функция function4")
    return 3**x

x = 4
res = function4(4)
print(f"3 в степени {x} = {function4(4)}")

# Функция - калькулятор индекса массы тела
def bmi (name, weight, height) : 
    res = weight/(height**2)
    if res > 18 and res < 25 : 
        return f"У человека с именем {name} нормальный вес: bmi = {res}"
    elif res <= 18 : 
        return f"У человека с именем {name} истощение: bmi = {res}"
    elif res > 30 : 
        return f"У человека с именем {name} ожирение: bmi = {res}"
    else: 
        return f"У человека с именем {name} избыточный вес: bmi = {res}"

print(bmi("Таня", 72, 1.68))
print(bmi("Катя", 48, 1.56))
print(bmi("Таня", 72, 1.68), ",\n", bmi("Таня", 72, 1.68))



