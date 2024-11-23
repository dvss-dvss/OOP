class Pet:
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
        ans = "Об'єкт класу Pet\n"
        ans += "Ім'я: " + self.name + "\n"
        return ans

def main():
    print("Створення звірят.")
    pet1 = Pet("Звірятко 1")
    pet2 = Pet("Звірятко 2")
    pet3 = Pet("Звірятко 3")

    Pet.status()

    print("Доступ до властивості об'єкта:", pet1.mood)

main()