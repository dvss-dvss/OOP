class Pet:
    """Віртуальний вихованець"""

    def talk(self):
        print("Привіт. Я - звірятко")

def main():
    pet = Pet()
    pet.talk()

main()