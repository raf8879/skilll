import random

# Создаем класс Ship для представления кораблей
class Ship:
    def __init__(self, x, y, length, direction):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction

# Создаем класс Board для игровой доски
class Board:
    def __init__(self):
        self.size = 6
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []

    def is_valid_location(self, x, y, length, direction):
        if direction == 'горизонтально':
            return 0 <= x < self.size and 0 <= y < self.size and y + length <= self.size
        else:
            return 0 <= x < self.size and 0 <= y < self.size and x + length <= self.size

    def place_ship(self, ship):
        if self.is_valid_location(ship.x, ship.y, ship.length, ship.direction):
            if ship.direction == 'горизонтально':
                for i in range(ship.length):
                    if self.grid[ship.x][ship.y + i] != ' ':
                        raise ValueError("Корабли пересекаются!")
                    self.grid[ship.x][ship.y + i] = 'S'
            else:
                for i in range(ship.length):
                    if self.grid[ship.x + i][ship.y] != ' ':
                        raise ValueError("Корабли пересекаются!")
                    self.grid[ship.x + i][ship.y] = 'S'
            self.ships.append(ship)
        else:
            raise ValueError("Корабль выходит за границы доски или пересекает другие корабли")

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
            print("-" * (self.size * 4 - 1))

# Функция для создания случайного корабля
def random_ship(length):
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    direction = random.choice(['горизонтально', 'вертикально'])
    return Ship(x, y, length, direction)

# Создаем доски для игрока и компьютера
player_board = Board()
computer_board = Board()

# Расставляем корабли на досках
for ship_length in [3, 2, 2, 1, 1, 1, 1]:
    while True:
        ship = random_ship(ship_length)
        try:
            player_board.place_ship(ship)
            break
        except ValueError:
            continue

for ship_length in [3, 2, 2, 1, 1, 1, 1]:
    while True:
        ship = random_ship(ship_length)
        try:
            computer_board.place_ship(ship)
            break
        except ValueError:
            continue

# Основной цикл игры
player_hits = 0
computer_hits = 0

while True:
    print("Доска игрока:")
    player_board.display()
    print("\nДоска компьютера:")
    computer_board.display()

    try:
        x = int(input("Введите номер строки (0-5): "))
        y = int(input("Введите номер столбца (0-5): "))
    except ValueError:
        print("Введите целые числа от 0 до 5.")
        continue

    # Проверка, что введенные координаты находятся в пределах поля
    if not (0 <= x < 6) or not (0 <= y < 6):
        print("Координаты выходят за границы поля. Введите корректные координаты.")
        continue

    # Проверка попадания игрока
    if computer_board.grid[x][y] == 'S':
        print("Попадание!")
        computer_board.grid[x][y] = 'X'
        player_hits += 1
        if player_hits == 10:
            print("Игрок победил!")
            break
    else:
        print("Промах!")

    # Ход компьютера
    while True:
        comp_x = random.randint(0, 5)
        comp_y = random.randint(0, 5)
        if player_board.grid[comp_x][comp_y] == 'S':
            print("Компьютер попал!")
            player_board.grid[comp_x][comp_y] = 'X'
            computer_hits += 1
            if computer_hits == 10:
                print("Компьютер победил!")
                break
            break
        elif player_board.grid[comp_x][comp_y] == ' ':
            print("Компьютер промахнулся!")
            player_board.grid[comp_x][comp_y] = 'T'
            break

    input("Нажмите Enter для продолжения...")