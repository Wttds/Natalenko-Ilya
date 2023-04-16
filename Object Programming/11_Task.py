# Write code here
from random import randint, choice


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x, self._y = x, y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length
        self._coords, self._coords_around = [], []
        if self._x is not None and self._y is not None:
            if self._tp == 1:
                self._coords = set((a, self._y) for a in range(self._x, self._x + length))
                self._coords_around = set((a, b) for a in range(self._x - 1, self._x + length + 1)
                                      for b in range(self._y - 1, self._y + 2))
            else:
                self._coords = set((self._x, b) for b in range(self._y, self._y + length))
                self._coords_around = set((a, b) for a in range(self._x - 1, self._x + 2)
                                      for b in range(self._y - 1, self._y + length + 1))

    def get_start_coords(self):
        return (self._x, self._y)

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def is_collide(self, ship):
        for coords in self._coords:
            if coords in ship._coords_around:
                return True
        return False

    def is_out_pole(self, size=10):
        for coords in self._coords:
            if coords[0] < 0 or coords[0] >= size or coords[1] < 0 or coords[1] >= size:
                return True
        return False

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def __getitem__(self, indx):
        return self._cells[indx]

    def __setitem__(self, indx, value):
        self._cells[indx] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))]


        for ship in self._ships:
            valid = False
            while not valid:
                valid = True
                ship.__init__(ship._length, ship._tp, randint(0, self._size - 1), randint(0, self._size - 1))
                for other_ship in list(filter(lambda s: id(s) != id(ship), self._ships)):
                    if ship.is_collide(other_ship) or ship.is_out_pole(self._size):
                        valid = False
                        break

    def get_ships(self):  # Геттер
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            go = choice([-1, 1])
            ship.move(go)
            ship.__init__(ship._length, ship._tp, ship._x, ship._y)
            for other_ship in list(filter(lambda s: id(s) != id(ship), self._ships)):
                if ship.is_collide(other_ship) or ship.is_out_pole(self._size):
                    go = -go
                    break
            ship.move(go)
            ship.move(go)
            ship.__init__(ship._length, ship._tp, ship._x, ship._y)
            for other_ship in list(filter(lambda s: id(s) != id(ship), self._ships)):
                if ship.is_collide(other_ship) or ship.is_out_pole(self._size):
                    go = -go
            ship.move(go)

    def show(self):
        self._pole = {x: {y: 0 for y in range(self._size)} for x in range(self._size)}
        for x in range(self._size):
            for y in range(self._size):
                if (x, y) in list(map(lambda c: c._coords, self._ships)):
                    self._pole[x][y] = 1
                print(self._pole[x][y], end=" ")
            print()

    def get_pole(self):
        all_ships_coords = list(map(lambda o: o._coords, self._ships))
        l = []
        for s in all_ships_coords:
            l += list(s)
        tup = []
        for a in range(self._size):
            tup.append([])
            for b in range(self._size):
                tup[a].append(1) if (a, b) in l else tup[a].append(0)
        tup = tuple(map(lambda o: tuple(o), tup))
        return tup

    def __str___(self):
        field = self.get_pole()
        for row in field:
            for col in row:
                print(field[row][col], end=' ')
            print()
                

# Tests
# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# pole.show()
#
# pole.move_ships()
# print()
# pole.show()

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
