class Car:
    #attributes
    #functionalities (methods)
    def __init__(self, make, year_value, mil, color, body, speed=0):
        self.make = make
        self.year = year_value
        self.milage = mil
        self.color = color
        self.body = body
        self.__speed = speed #now speed is private

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self.__speed = 0

    def decelerate(self):
        if self.__speed <= 10: #prevents this function from causing it to be -.
            self.__speed = 0

        else:
            self.__speed -= 10

    def park():
        pass