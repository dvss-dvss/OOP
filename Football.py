class FootballPlayer:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}({self.position})"
    
def main():
    team = []
    for i in range(1, 12):
        name = input("Ім'я  для футболіста з №" + str(i) + " : ")
        position = input("Позиція для футболіста з №" + str(i) + " : ")
        team.append(FootballPlayer(name,position))
    print(*team, sep=", ")

main()
