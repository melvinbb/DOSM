from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    def __init__(self, platform):
        self.platform = platform

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Выполняется оплата кредитной картой на сумму {amount} через платформу {self.platform.get_platform()}")
        self.platform.process_payment(amount)


class Platform(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def get_platform(self):
        pass


class MobileAppPlatform(Platform):
    def process_payment(self, amount):
        print(f"Обработка платежа на сумму {amount} в мобильном приложении.")

    def get_platform(self):
        return "Mobile App"


class WebPlatform(Platform):
    def process_payment(self, amount):
        print(f"Обработка платежа на сумму {amount} на веб-сайте.")

    def get_platform(self):
        return "Web Platform"


if __name__ == "__main__":
    print("Выберите платформу:")
    print("1. Мобильное приложение")
    print("2. Веб-сайт")
    platform_choice = input("Введите номер платформы (1-2): ")

    if platform_choice == "1":
        platform = MobileAppPlatform()
    elif platform_choice == "2":
        platform = WebPlatform()
    else:
        print("Неверный выбор платформы.")
        exit()

    print("Выберите способ оплаты:")
    print("1. Кредитная карта")
    print("2. Электронный кошелек")
    payment_choice = input("Введите номер способа оплаты (1-2): ")

    if payment_choice == "1":
        payment_method = CreditCardPayment(platform)
    elif payment_choice == "2":
        payment_method = EWallerPayment(platform)
    else:
        print("Неверный выбор способа оплаты.")
        exit()

    amount = float(input("Введите сумму платежа: "))
    payment_method.process_payment(amount)
