class Obiekt:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("Coordinates: ", self.x, self.y)


class Owoc(Obiekt):
    jedzenie = 0

    def __init__(self, x, y, jedzenie):
        self.jedzenie = jedzenie
        self.x = x
        self.y = y

    def print(self):
        print("I'm a fruit with level ", self.jedzenie, "Coordinates: ",
              self.x, self.y)


class Robaczek(Obiekt):
    speed = 0
    level = 0
    food = 0

    def __init__(self, x, y, speed, level, food):
        self.speed = speed
        self.level = level
        self.food = food
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def print(self):
        print("I'm a worm")
        print("x: ", self.x)
        print("y: ", self.y)
        print("speed: ", self.speed)
        print("level: ", self.level)
        print("food: ", self.food)

    def zjedzOwoc(self, owoc):
        self.food += owoc.jedzenie
        self.level += owoc.jedzenie
        self.checkLevel()

    def checkLevel(self):
        if self.food >= self.level * 2:
            print("I'm stronger!")
            self.speed += 1


def checkObjectsAndEat(robaczek, owoc):
    if robaczek.x == owoc.x and robaczek.y == owoc.y:
        robaczek.zjedzOwoc(owoc)
        return True
    return False


def printAll():
    for obj in lista:
        obj.print()
    robaczek.print()


lista = []
file = open("stan_gry.txt", "r")
index = 0
robaczek = Robaczek(0, 0, 0, 0, 0)
for line in file:
    data = line.replace("\n", "").split(",")
    if 0 < index:
        lista.append(Owoc(int(data[0]), int(data[1]), int(data[2])))
    else:
        robaczek = Robaczek(int(data[0]), int(data[1]), int(data[2]),
                            int(data[3]), int(data[4]))
    index += 1

while lista:
    printAll()
    arrow = input("Where should i move? [AWSD]: ")
    if ("w" == arrow):
        robaczek.move(0, 1)
    elif ("s" == arrow):
        robaczek.move(0, -1)
    elif ("a" == arrow):
        robaczek.move(-1, 0)
    elif ("d" == arrow):
        robaczek.move(1, 0)
    else:
        print("Wrong input")
        continue
    for key, owoc in enumerate(lista):
        if checkObjectsAndEat(robaczek, owoc):
            del lista[key]

print("Congratulations, you won!")
printAll()