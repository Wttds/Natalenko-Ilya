# Write code here
from random import randint, choice


class Ship:
    def __init__(self, length, tp=1, x=None, y=None): # tp=1 - горизонтально, tp=2 - вертикально
        self._x, self._y = x, y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(length)]

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    # Возвращает True, если корабли пересекаются, в противном случае False
    def is_collide(self, other):
        gabarites_1, gabarites_2 = [], []

        if self._tp == 1:
            for a in range(-1, 2):
                gabarites_1 += [(x, self._y + a) for x in range(self._x - 1, self._x + self._length + 1)]
            gabarites_2 += [(x, other._y) for x in range(other._x, other._x + other._length)]
        else:
            for a in range(-1, 2):
                gabarites_1 += [(self._x, y) for y in range(self._y - 1, self._y + self._length + 1)]
            gabarites_2 += [(other._x, y) for y in range(other._y, other._y + other._length)]

        intersection = set(gabarites_1).intersection(set(gabarites_2))
        return len(intersection) > 0
        # Корабли не могут пересекаться, если их типы различны

        # if self._tp == 1 and other._tp == 1:  # оба корабля горизонтальные
        #     if self._y != other._y:  # корабли на разных строках
        #         return False
        #     if self._x > other._x:
        #         self, other = other, self  # self должен быть слева
        #     return self._x + self._length > other._x
        # elif self._tp == 2 and other._tp == 2:  # оба корабля вертикальные
        #     if self._x != other._x:  # корабли в разных столбцах
        #         return False
        #     if self._y > other._y:
        #         self, other = other, self  # self должен быть сверху
        #     return self._y + self._length > other._y
        # else:  # корабли перпендикулярны
        #     if self._tp == 1:  # self - горизонтальный, other - вертикальный
        #         horiz, vert = self, other
        #     else:  # self - вертикальный, other - горизонтальный
        #         horiz, vert = other, self
        #     if horiz._y <= vert._y <= horiz._y + horiz._length and \
        #             vert._x <= horiz._x <= vert._x + vert._length:
        #         return True
        # return False
        # coo1 = []
        # if self._tp == 1:
        #     for i in range(-1, 2):
        #         coo1 += [(x, self._y + i) for x in range(self._x - 1, self._x + self._length + 1)]
        # else:
        #     for i in range(-1, 2):
        #         coo1 += [(self._x + i, y) for y in range(self._y - 1, self._y + self._length + 1)]
        #
        # if other._tp == 1:
        #     coo2 = [(x, other._y) for x in range(other._x, other._x + other._length)]
        # else:
        #     coo2 = [(other._x, y) for y in range(other._y, other._y + other._length)]
        #
        # return len(set(coo1) & set(coo2)) > 0

    # Возвращает True, если корабль хотя бы частично находитсся вне поля, в противном случае False
    def is_out_pole(self, size):
        pole = [(x, y) for x in range(size) for y in range(size)]

        if self._tp == 1:
            ship = [(x, self._y) for x in range(self._x, self._x + self._length)]
        else:
            ship = [(self._x, y) for y in range(self._y, self._y + self._length)]

        return len(set(ship) - set(pole)) > 0

    def __getitem__(self, key):
        return self._cells[key]

    def __setitem__(self, key, value):
        self._cells[key] = value

class GamePole():
    # Инициализация класса
    def __init__(self, size=10):
        self._size = size
        self._ships = []

    # Инициализация самого поля
    def init(self):
        for i in range(1, 5):       # Количество палуб
            for j in range(5 - i):  # Количество i-палубных кораблей
                while True:
                    ship = Ship(length=i, tp=randint(1,2))
                    x, y = randint(0, self._size - 1), randint(0, self._size - 1)
                    ship.set_start_coords(x, y)
                    if not (ship.is_out_pole(self._size) or any([ship.is_collide(other) for other in self._ships])):
                        self._ships.append(ship)
                        break

    def get_ships(self):
        return self._ships

    def fill_pole(self):
        ships_coords, pole = [], []
        for ship in self._ships:  # Узнаём координаты всех палуб всех кораблей
            for p in range(ship._length):
                if ship._tp == 1:
                    ships_coords.append((ship._x + p, ship._y))
                else:
                    ships_coords.append((ship._x, ship._y + p))

        for y in range(self._size):  # Смотрим, какие координаты есть в списке палуб и ставим 1, если есть, иначе 0
            pole.append([])
            for x in range(self._size):
                if (x, y) in ships_coords:
                    pole[y].append("1")
                else:
                    pole[y].append("0")
        return pole

    # Вывод доски с кораблями
    def show(self):
        pole = self.fill_pole()
        for row in pole:
            print(*row)

    # Получение доски в виде двумерного кортежа
    def get_pole(self):
        pole = self.fill_pole()
        for row in range(len(pole)):
            pole[row] = tuple(pole[row])
        return tuple(pole)

    def move_ships(self):
        for i, ship in enumerate(self._ships):
            if ship._is_move:
                step = choice([-1, 1])
                ship.move(step)
                if ship.is_out_pole(self._size) or any([ship.is_collide(s) for s in self._ships[:i] + self._ships[i+1:]]):
                    ship.move(-(2 * step))
                    if ship.is_out_pole(self._size) or any([ship.is_collide(s) for s in self._ships[:i] + self._ships[i+1:]]):
                        ship.move(step)
                

# Tests
SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()

# Tests
ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)
assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"
ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"
p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
pole_size_8 = GamePole(8)
pole_size_8.init()
print("\n Passed")
