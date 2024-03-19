a = [1, 2, 3, 4, 5]
print(a)
# Создадим список b, каждый элемент которого будет в два раза больше 
# соответствующего элемента списка a
b = []
for num in a : 
    b.append(num*2)
print(b)

# Когда у нас есть некоторая последовательность элементов, и мы на ее основе 
# хотим создать некоторую другую последовательность, лучше и проще всего 
# использовать генераторы списков (или ListComprehensions)

c = [num*2 for num in a]
print(c)

d = [i*3 for i in range(1, 6)]
print(d)

a = [1, 10 , 12, 4, 3, 20, 55]
# Давайте выберем из этого списка все те значения, которые меньше 10: 
print(a)
b = [num for num in a if num < 10]
print(b)

# Поработаем теперь со списком слов: 
words = ['hello', 'hey', 'good bye', 'guitar', 'piano']
# Отфильтруем в нем те слова, длина которых менее 6 символов

less_than_six = [word for word in words if len(word) < 6]
print(less_than_six)

# Задача: 
# Пройтись по всем четным числам от 10 до 2 и каждое из них умножить на 2
doubled_evens = [num*2 for num in range(10, 0, -2)]
print(doubled_evens)

# Задача: 
# К каждому слову из списка words, длина которого больше 5-ти, добавить точку в конце

point_marks_words_longer_than_5 = ["".join([word, "."]) if len(word) > 5 else word for word in words ]
print(point_marks_words_longer_than_5)

