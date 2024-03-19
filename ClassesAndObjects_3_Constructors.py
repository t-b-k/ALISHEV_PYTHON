# КОНСТРУКТОРЫ

class Person : 
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
# p1.name = "Elon"
# p1.surname = "Mask"
# p1.place_of_birth = "ЮАР"
# p1.year_of_birth = 1971

p2 = Person("Sergey", "Korolev", "Российская Империя", 1907)
p2.name = "Sergey"
p2.surname = "Korolev"
p2.place_of_birth = "Российская Империя"
p2.year_of_birth = 1907

# Такой способ создания объектов не очень хорош, так как он провоцирует появление 
# ошибок: 
# пользователь может ошибиться в написании названия поля (тем самым у объекта появится новое 
# поле, не используемое ни в одном из методов); он может забыть присвоить значение некоторому полю, 
# которое используется некоторыми методами, и т.п. Поэтому желательно создать унифицированный метод-конструктор, 
# который будет одинаковым образом реализовывать создание объекта на основе задаваемых пользователем значений 
# атрибутов объекта. 
# Кроме того, здесь мы наблюдаем бесконечное дублирование кода. 

# Конструктор объектов определяется в описании класса, и он автоматически (неявно) вызывается при создании нового объекта. 
# Название у конструктора также фиксированное: __init__()
# Аргументы - любые
# Описание конструктора в классе должно предшествовать описанию всех других методов этого класса

p3 = Person("Albert", "Einstein", "Германия", 1879)

p1.print_info()
Person.print_info(p2)
print(f"Name: {p3.name:10} Surname: {p3.surname:10} Place of birth: {p3.place_of_birth:10}")

# Интересно, что любому из этих объектов мы по-прежнему можем добавлять новые поля на свое усмотрение






