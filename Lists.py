# СПИСКИ

# list - это такой тип данных, который внутри себя хранит значения других типов данных, 
# такой "ящик", который внутри себя содержит объекты
# __Упорядоченный__ __изменяемый__ набор элементов
# Элементы могут быть разных типов
# Элементы проиндексированы и доступны по индексу
# Допустима вложенность списков и прочих типов наборов данных
# Список создается при помощи квадратных скобок (явно) или неявно - при помощи оператора list()
# При выводе на экран список заключается также в квадратные скобки

a = [3, 5, 7]
print(a)

# ДОБАВЛЕНИЕ ЭЛЕМЕНТА В КОНЕЦ СПИСКА: 
a.append(15)
print(a)
a.append("Hi!")
print(a)
a.append([5,6])
print(a)

# УДАЛЕНИЕ ПОСЛЕДНЕГО ЭЛЕМЕНТА СПИСКА
a.pop() # последний элемент удаляется по умолчанию
print(a)

# УДАЛЕНИЕ ОПРЕДЕЛЕННОГО ЭЛЕМЕНТА СПИСКА
a.pop(0)  # производится по индексу

# Обращение к элементу списка - по индексу: 
print(a[1], a[3])

# Допустимо отрицательное индексирование: 
print(a[-1])    # будет выведен последний элемент списка
print(a[-2])    # Второй с конца
a[1] = 100
print(a)



