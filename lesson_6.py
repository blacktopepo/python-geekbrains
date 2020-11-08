class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self):
        color_list = ['красный', 'желтый', 'зеленый']
        self.__color = color_list[(color_list.index(self.__color) + 1) % 3]
        print(self.__color)

    def __str__(self):
        return self.__color


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        mass_square_meter = 25
        height = 5
        return self._length * self._width * mass_square_meter * height / 1000

    def __str__(self):
        return f'Масса асфальта: {self.mass_of_asphalt()} кг'


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int,
                 bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name.title()} {self.surname.title()}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f'{self.get_full_name()}\nДоход: {self.get_total_income()}'


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police



if __name__ == '__main__':
    traffic_light = TrafficLight()
    print(traffic_light)
    traffic_light.running()
    traffic_light.running()

    road = Road(20, 5000)
    print(road)

    position = Position('Alex', 'Block', 'manager', 10000, 5000)
    print(position)



