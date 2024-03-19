# Определим функцию печати информации о человеке в классе Person

class Person : 
    def print_info(self) : 
        print(f"Name: {self.name} Surname: {self.surname} Place of birth: {self.place_of_birth}")
    def get_age(self, crnt_year) : 
        return crnt_year - self.year_of_birth
p1 = Person()
p1.name = "Elon"
p1.surname = "Mask"
p1.place_of_birth = "ЮАР"
p1.year_of_birth = 1971

p2 = Person()
p2.name = "Sergey"
p2.surname = "Korolev"
p2.place_of_birth = "Российская Империя"
p2.year_of_birth = 1907

print(p1.name)
print(p2.name)

p1.print_info()
p2.print_info()

# Альтернативный способ: 
Person.print_info(p1)
Person.print_info(p2)

print(Person.get_age(p1, 2024))
print(p2.get_age(2024))
