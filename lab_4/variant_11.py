from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, package_weight, distance):
        pass


class CourierDelivery(DeliveryStrategy):
    def calculate_cost(self, package_weight, distance):
        return 10 * (package_weight * 2) + (distance * 0.5)


class PostalDelivery(DeliveryStrategy):
    def calculate_cost(self, package_weight, distance):
        return 5 + (package_weight * 1) + (distance * 0.2)


class DroneDelivery(DeliveryStrategy):
    def calculate_cost(self, package_weight, distance):
        if package_weight > 2:
            return "Дроны не могут доставлять посылки весом более 2 кг."
        else:
            return 20 + (distance * 1)


class DeliveryContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate_delivery_cost(self, package_weight, distance):
        return self.strategy.calculate_cost(package_weight, distance)


if __name__ == "__main__":
    print("Выберите стратегию доставки:")
    print("1. Курьерская доставка")
    print("2. Почтовая доставка")
    print("3. Доставка дронами")
    choice = input("Введите номер стратегии (1-3): ")
    if choice == "1":
        strategy = CourierDelivery()
    elif choice == "2":
        strategy = PostalDelivery()
    elif choice == "3":
        strategy = DroneDelivery()
    else:
        print("Неверный выбор стратегии.")
        exit()
    context = DeliveryContext(strategy)
    package_weight = float(input("Введите вес посылки (кг): "))
    distance = float(input("Введите расстояние доставки (км): "))
    cost = context.calculate_delivery_cost(package_weight, distance)
    print("Стоимость доставки:", cost)
