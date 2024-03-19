# НАСЛЕДОВАНИЕ

# Ранее мы создавали не связанные друг с другом классы. 
# Но в жизни все намного сложнее, и одни сущности зачастую являются подвидом других. 

# I. ОТНОШЕНИЕ "IS A" (ЯВЛЯЕТСЯ)

#                             ЧЕЛОВЕК
#     /           /           /           \              \
# СТУДЕНТ     УЧИТЕЛЬ     ПРОДАВЕЦ        ПОКУПАТЕЛЬ      ВРАЧ

# И студенты, и учителя, и продавцы, и покупатели, и врачи - это все ЛЮДИ, 
# и каждый из  них обладает всеми атрибутами человека. 

# Как наследники класса Person, все эти классы будут обладать всеми атрибутами и 
# реализовывать все методы данного класса

class Person : 
    def __init__(self, name, age) :
        self.name = name
        self.age = age 
        print(f"Person of class {type(self)} with name {name} of age {age} years old is created")

    def say_hello(self) : 
        print(f"{self.name}. Наше вам с кисточкой!")

p1 = Person("Tom", 15)
p1.say_hello()

# Чтобы унаследовать класс Student от класса Person, надо просто написать: 

class Student(Person) : 
    def __init__(self, name, age, average_grade) :
        # Person.__init__(self, name, age) <==>
        super().__init__(name, age) # super() - это объект родительского класса, поэтому self передавать уже не надо
        self.average_grade = average_grade
        print(f"Student {self.name} is created")

    def study(self) : 
        print(f"{self.name} учится на {self.average_grade}")
    
    def say_hello(self):
        print(f"{self.name}, студент. Приветствую вас!!!")

class Teacher(Person) : 
    def teach(self): 
        print(f"{self.name} преподает")

s1 = Student("Дима Петров", 20, 3)
s2 = Student("Сергей Власов", 60, 5)
t1 = Teacher("Мария Ивановна, математик", 80)
s1.study()
s2.study()
t1.teach()
Person.say_hello(t1)
Person.say_hello(s2)
s1.say_hello()

# А что будет, если мы в классе Student реализуем метод с таким же именем, как и тот, что определен в классе Person? 

# Определим теперь внешнюю функцию introduce на классе объектов Person, 
# и посмотрим, как она будет работать на объектах разных классов

def introduce(person) : 
    print(f"Сейчас персона по имени {person.name} поприветствует вас...")
    person.say_hello()

introduce(p1)
introduce(s1)
introduce(s2)
introduce(t1)

people_array = [Person("Тамара Петровна", 91), Student("Валя Котик", 17, 4), Teacher("Леонид Исаакович", 80), Student("Ольга Логинова", 54,3)]

for person in people_array : 
    introduce(person)

# Задача. 
# Определить класс Animal c атрибутом name и методом eat() => "Animal {self.name} is eating"
# Создать классы-наследники: Dog, Cat и Frog такие, что: 
# Dog: + атрибут breed, + метод bark()
# Cat: + метод meow()
# Frog: ~ метод eat() => "Frog is eating"
    
class Animal : 
    def __init__(self, name) : 
        self.name = name
    
    def eat(self) :
        print(f"Animal {self.name} is eating...")

class Dog(Animal) : 
    def __init__ (self, name, breed) : 
        super().__init__(name)
        self.breed = breed

    def bark(self) : 
        print(f"Dog {self.name} is barking...")
    
    # def bark() : 
    #     print("Dog is barking")

class Cat(Animal) : 
    def meow(self) : 
        print(f"Cat {self.name} is meowing...")

class Frog(Animal) : 
    def eat(self) : 
        print("FROG is eating")

animals = [Cat("Василий"), Dog("Себастьян", "цвергшнауцер"), Frog("Квакуша"), Dog("Шуша", "корги"), Cat("Фадей")]
for animal in animals : 
    if isinstance(animal, Dog) : 
        animal.bark()
    elif isinstance(animal, Cat) : 
        animal.meow()
    animal.eat()