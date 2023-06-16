class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} прошел {traveled} км за {time} ч, при скорости {self.speed} км/ч")


class CrawlerRobot(Robot):
    def __init__(self, territory, name, speed):
        super().__init__(name, speed)
        self.territory = territory

    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} пршел {traveled} км по {self.territory} за {time} ч, при скорости {self.speed} км/ч")


class RobotOnWheels(Robot):
    def __init__(self, model, name, speed):
        super().__init__(name, speed)
        self.model = model

    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} марки {self.model} прошел {traveled} км за {time} ч, при скорости {self.speed} км/ч")


usual_robot = Robot('wallie', 5)
usual_robot.movement(10)

tank_robot = CrawlerRobot('Полигон', 'Т-90', 40)
tank_robot.movement(6)

car_robot = RobotOnWheels('BMW', 'X-7', 100)
car_robot.movement(12)
