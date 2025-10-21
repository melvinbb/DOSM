from abc import  ABC, abstractmethod
import time
class Observer(ABC):
    @abstractmethod
    def update(self, sensor_type, sensor_value):
        pass
class AlarmSystem(Observer)
    def update(self, sensor_type, sensor_value):
        if sensor_type == "Движение":
            print(f"Сигнализация: Обнаружено движение! ({sensor_value})")
        if sensor_type == "Дым":
            print(f"Сигнализация: Дверь открыта! ({sensor_value})")
        if sensor_type == "Открытие двери":
            print(f"Сигнализация: Дверь открыта! ({sensor_value})")
