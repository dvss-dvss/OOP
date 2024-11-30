# Моє звірятко


class Pet:
    """Віртуальниц  вихованець"""
    total = 0

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "непогано"
        elif 11 <= unhappiness <= 15:
            m = "не сказати щоб добре"
        else:
            m = "жахливо"
        return m
    
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
        print("Мене звати", self.__name,", і зараз я почуваюся", self.mood )
        self.__pass_time()

    def eat(self, food = 4):
        print("Мррр... Дякую!")
        self.hunger -= food
        if self.hunger <0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Уііі!")
        self.boredom -= fun
        if self.boredom <0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        return f"{self.name}({self.hunger=}, {self.boredom=})"

def main():
    pet_name = input("Як ви назвете своє звірятко?: ")
    pet = Pet(pet_name)

    choice = None
    while choice != "0":
        print \
        ("""
         Моє звірятко
         
         0 - Вийти
         1 - Дізнатися про самопочуття звірятка
         2 - Годувати звірятко
         3 - Пограти зі звірятком
         """)
        
        choice = input("Ваш вибір: ")
        print()

        # Вихід
        if choice == "0":
            print("До побачення.")

        # Бесіда зі звіртком
        elif choice == "1":
            pet.talk()

        # Годування звірятка
        elif choice == "2":
            pet.eat(int(input("Скількі шматочків буде: ")))

        # Гра зі звірятком
        elif choice == "3":
            pet.play(int(input("Скільки часу пограємось:")))
        
        # Секретний пункт
        elif choice =="7":
            print(pet)

        # Незрозуміле введення користувача
        else:
            print("Вибачте, у мене немає пункту", choice)

main()