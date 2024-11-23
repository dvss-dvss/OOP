class Pet:
    total = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Ім'я звірятка не може бути порожнім рядком.")
        else:
            self.__name = new_name
            print("Ім'я успішно змінено.")

    @staticmethod
    def status():
        print("Загальна кількість звірят", Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Pet.total += 1

    def talk(self):
        print("Мене звати", self.__name)

    def __str__(self):
        ans = "Об'єкт класу Pet\n"
        ans += "Ім'я: " + self.name + "\n"
        return ans

def main():
    print("Доступ до атрибуту класу Pet.total:", end=" ")
    print(Pet.total)

    print("Створення звірят.")
    pet1 = Pet("Звірятко 1")
    pet2 = Pet("Звірятко 2")
    pet3 = Pet("Звірятко 3")

    Pet.status()

    print("Доступ до атрибуту класу через об'єкт:", end=" ")
    print(pet1.total)

main()