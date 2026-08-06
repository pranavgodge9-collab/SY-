class CreditCard:
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")

class DebitCard:
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Debit Card.")

class UPI:
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using UPI.")

class NetBanking:
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Net Banking.")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

amount = float(input("Enter payment amount: "))

print("\nChoose Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")

choice = int(input("Enter your choice: "))

if choice == 1:
    payment = PaymentProcessor(CreditCard())
elif choice == 2:
    payment = PaymentProcessor(DebitCard())
elif choice == 3:
    payment = PaymentProcessor(UPI())
elif choice == 4:
    payment = PaymentProcessor(NetBanking())
else:
    print("Invalid Choice")
    exit()

payment.process_payment(amount)
