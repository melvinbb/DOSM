from abc import ABC, abstractmethod
class Customer(ABC):
    @abstractmethod
    def update(self, product):
        pass
class RegularCustomer(Customer):
    def __init__(self, name):
        self.name = name
    def update(self, product):
        print(f"Уважаемый {self.name}, появился новый товар: {product}")
class VIPCustomer(Customer):
    def __init__(self, name):
        self.name = name
    def update(self, product):
        print(f"Внимание, {self.name}! Специально для вас - новый товар: {product}! Спешите приобрести!")
class Store:
    def __init__(self):
        self.products = []
        self.customers = []
    def subscribe(self, customer):
        self.customers.append(customer)
    def unscribe(self,customer):
        self.customers.remove(customer)
    def add_product(self, product):
        self.products.append(product)
        self.notify_customers(product)
    def notify_customers(self, product):
        for customer in self.customers:
            customer.update(product)
if __name__ == "__main__":
    store = Store()
    customer1 = RegularCustomer("Иван")
    customer2 = VIPCustomer("Анна")
    customer3 = RegularCustomer("Петр")
    store.subscribe(customer1)
    store.subscribe(customer2)
    store.add_product("Новый смартфон Galaxy X")
    store.add_product("Умные часы iWatch Pro")
    store.unscribe(customer1)
    store.add_product("Беспроводные наушники AirBeats Z")