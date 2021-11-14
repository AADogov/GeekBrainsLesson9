# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# ----------Решение-------------
# создаем класс Stationery
class Stationery:

    # обявляем атрибуты класса
    def __init__(self, t):
        self.title = t

    # обявляем методы класса
    def draw(self):
        print("Draw starts.")


# создаем  дочерний для класса Stationery - клас Pen
class Pen(Stationery):

    # обявляем атрибуты класса
    def __init__(self, t):
        super().__init__(t)

    # обявляем методы класса
    def draw(self):
        print("Pen starts.")


# создаем  дочерний для класса Stationery - клас Pencil
class Pencil(Stationery):

    # обявляем атрибуты класса
    def __init__(self, t):
        super().__init__(t)

    # обявляем методы класса
    def draw(self):
        print("Pencil starts.")


# создаем  дочерний для класса Stationery - клас Handle
class Handle(Stationery):

    # обявляем атрибуты класса
    def __init__(self, t):
        super().__init__(t)

    # обявляем методы класса
    def draw(self):
        print("Handle starts")


# проверяем
stationery_1 = Stationery("Flags kit")
pen_1 = Pen('Blue pen')
pencil_1 = Pencil('Red pencil')
handle_1 = Handle("Black handle")

stationery_1.draw()
pen_1.draw()
pencil_1.draw()
handle_1.draw()
