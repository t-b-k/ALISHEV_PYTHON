# АТРИБУТЫ КЛАССА

# Атрибут класса - это атрибут, который разделяют все объекты одного класса. 
# Он определяется в описании класса. 

class Person : 
    some_num = 123

    def __init__(self, name, surname, place, year) : 
        self.name = name
        self.surname = surname
        self.place_of_birth = place
        self.year_of_birth = year

    def print_info(self) : 
        print(f"Name: {self.name} Surname: {self.surname} Place of birth: {self.place_of_birth}")
    def get_age(self, crnt_year) : 
        return crnt_year - self.year_of_birth
    
p1 = Person("Elon", "Mask", "ЮАР", 1971)
p1.test = "Hello!"
print(f"p1.test = {p1.test}")
print(f"p1.some_num = {p1.some_num}")
# p1.name = "Elon"
# p1.surname = "Mask"
# p1.place_of_birth = "ЮАР"
# p1.year_of_birth = 1971

p2 = Person("Sergey", "Korolev", "Российская Империя", 1907)
p2.name = "Sergey"
p2.surname = "Korolev"
p2.place_of_birth = "Российская Империя"
p2.year_of_birth = 1907
print(f"p2.some_num = {p2.some_num}")

# К атрибуту класса мы можем обращаться, даже не создавая объект этого класса: 
print(Person.some_num)

# Если мы через какой-нибудь объект изменим атрибут класса, то это изменение затронет 
# весь класс (все его объекты)
p3 = Person("Albert", "Einstein", "Германия", 1879)

p2.some_num = 456
print(f"p1.some_num = {p1.some_num}")
print(f"p2.some_num = {p2.some_num}")
print(f"p3.some_num = {p3.some_num}")

Person.some_num = 789
print(f"p1.some_num = {p1.some_num}")
print(f"p2.some_num = {p2.some_num}")
print(f"p3.some_num = {p3.some_num}")

# Почему так происходит? 
# Записью p2.some_num = 456 мы создали у ОБЪЕКТА p2 новый атрибут - some_num, 
# который "перекрыл" собой одноименный атрибут класса. 
# И теперь обращение p2.some_num является обращением к атрибуту объекта, в то время 
# как атрибут класса остался без изменения, что мы можем видеть через обращение к нему из других объектов, 
# в которых он не переопределялся. 

# Для чего могут использоваться атрибуты классов? 

# Предположим, мы хотим описать объект "Круг"

class Circle () : 
    PI = 3.14
    def __init__(self, radius) : 
        self.radius = radius

    def get_perimeter(self) : 
        return self.radius*2*Circle.PI
    def get_area(self) : 
        return Circle.PI*self.radius**2
    
c1 = Circle(3)
c2 = Circle(7)

print(f"c1 perimeter = {c1.get_perimeter()}")
print(f"c1 area = {c1.get_area()}")
print(f"c2 perimeter = {c2.get_perimeter()}")
print(f"c2 area = {c2.get_area()}")

# Создадим объект для подключения к базе данных: 
#class DB : 
    # Чтобы все объекты работали с одним подключением к базе данных, сделаем этот объект атрибутом класса: 
    # dbConnection = pass

    # def write_some_data(self) : pass

# Задача: модифицировать класс Person таким образом, чтобы в любой момент можно было узнать количество 
# созданных объектов этого класса. 
    
class Person1 : 
    num_of_persons = 0

    def __init__(self, name, surname, place, year) : 
        self.name = name
        self.surname = surname
        self.place_of_birth = place
        self.year_of_birth = year
        Person1.num_of_persons += 1

    def print_info(self) : 
        print(f"Name: {self.name} Surname: {self.surname} Place of birth: {self.place_of_birth}, qty of persons = {Person1.num_of_persons}")
    def get_age(self, crnt_year) : 
        return crnt_year - self.year_of_birth
    
p11 = Person1("Таня","Калашникова", "Москва", 1969)
p11.print_info()
p12 = Person1("Катя","Кузькина", "Москва", 1998)
Person1.print_info(p12)
p13 = Person1("Галина","Скулкина", "Ливны", 1945)
p13.print_info()
p14 = Person1("Борис","Калашников", "Москва", 1946)
Person1.print_info(p14)





