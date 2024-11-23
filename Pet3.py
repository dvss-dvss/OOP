class Pet:
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print("Мене звати", self.name)

    def __str__(self):
        ans = "Об'єкт класу Pet\n"
        ans += "Ім'я: " + self.name + "\n"
        return ans

def main():
    pet1 = Pet('Бобік')
    pet2 = Pet('Мурзик')
    print(pet1)

main()