
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Credit card payment of", amount, "processed.")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print("UPI payment of", amount, "processed.")


payment1 = CreditCardPayment()
payment2 = UPIPayment()

payment1.process_payment(1500)
payment2.process_payment(800)
