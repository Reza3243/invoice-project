print("Welcome to Invoice App!")
customer = input("Enter customer name: ")

item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total = quantity * price

print(f"\nInvoice for {customer}")
print(f"{quantity} x {item} = {total} EUR")print("Welcome to Invoice App!")
customer = input("Enter customer name: ")
print(f"Invoice for {customer}")
