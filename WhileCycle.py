# ЦИКЛ WHILE
total = 0
for i in range (1, 5) :
    total += i
print(total)

# В цикле while инициализация и инкрементирование счетчика являются задачей программиста
total1 = 0
i = 0
while i < 5 : 
    total1 += i
    i += 1
print(total1)

# В каких случаях цикл while полезен? 
# Когда мы не знаем заранее, сколько у нас будет итераций: это зависит от 
# какого-либо условия."""

my_list = sorted([1, 5, -2, 3, 45, -100, 75, -13, 2, 1, -7, 0])

# Если вам нужно изменить исходный список, используйте функцию sort(). 
# Если вам нужно сохранить оригинальный список и создать новый отсортированный список, используйте функцию sorted().
# Источник: https://uchet-jkh.ru/i/otliciya-mezdu-sort-i-sorted-v-python
print(my_list)
ind = 0
sum_of_negatives = 0 
while ind < len(my_list) and my_list[ind] < 0 : 
    sum_of_negatives += my_list[ind]
    ind += 1
print(f"Sum of negatives = {sum_of_negatives}")

# Для досрочного завершения цикла можно использовать оператор break

my_list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -13, -15, -18]
# Задача - с помощью цикла while и с помощью цикла for найти сумму всех отрицательных чисел в данном списке

sum = 0
i = -1
while i >= -len(my_list) and my_list[i] < 0 : 
    sum += my_list[i]
    i -=1
print(f"Сумма отрицательных элементов упорядоченного по убыванию списка равна {sum}")

sum = 0
for i in range(1,len(my_list)+1) : 
    if my_list[-i] >= 0 : 
        break
    sum += my_list[-i]
print(f"Сумма отрицательных элементов упорядоченного по убыванию списка равна {sum}")

words = ["apple", "banana", "grape", 'stop', "good by", "hello"]

for word in words : 
    if word == "stop" : 
        break
    print(word)

i = 0
while i < len(words) and words[i] != "stop" : 
    print(words[i])
    i += 1
    



