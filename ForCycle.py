# ЦИКЛ FOR

a = ['hey', 'hello', 'good by']
print(a[0])
print(a[1])
print(a[2])

# <==> 
for element in a : 
    print(element) 

b = [20, 30, 50, 60]
for num in b : 
    print(num, end=' ')

# Подсчитаем сумму элементов списка: 
sum = 0
for num in b : 
    sum += num
print(f"\nsum = {sum}")

# Воспользуемся функцией range
# range(i, j) - это диапазон всех целых чисел от i (включительно) до j (невключительно)
# range(j) - диапазон всех чисел от 0 до j: [0,j)

sum = 0
print(list(range(0, 4)))
for i in range(0,4) :
    print(sum, end=' ') 
    sum += b[i]
print(f"\nsum = {sum}")

for i in range(100) : 
    if i%3==0 : 
        print(i) 

all_numbers_aliquot_3 = [i for i in range(1,100) if i%3== 0]
print(all_numbers_aliquot_3)