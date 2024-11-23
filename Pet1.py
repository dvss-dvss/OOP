class Pet(object):
    """Віртуальний вихованець"""
    def __init__(self):
        print("З'явилось на світ звірятко")

    def talk(self):
        print("Привіт. Я - звірятко")

def main():
    pet1 = Pet()
    pet1.talk()
    pet2 = Pet()
    pet2.talk()

main()