from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def move(self):
        return "Автомобиль едет по дороге."


class Bicycle(Transport):
    def move(self):
        return "Велосипед едет по велосипедной дорожке."


class Plane(Transport):
    def move(self):
        return "Самолет летит по небу."


class TransportFactory:
    def create_transport(self, transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "bicycle":
            return Bicycle()
        elif transport_type == "plane":
            return Plane()
        else:
            raise ValueError("Неизвестный тип транспорта.")


if __name__ == "__main__":
    factory = TransportFactory()
    car = factory.create_transport("car")
    print(car.move())
    bicycle = factory.create_transport("bicycle")
    print(bicycle.move())
    plane = factory.create_transport("plane")
    print(plane.move())
    try:
        unknown = factory.create_transport("rocket")
    except ValueError as e:
        print(e)
