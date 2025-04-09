products = [
    {"name": "Iphone 16", "price": 1200},
    {"name": "Headphones", "price": 150},
    {"name": "Smartphone", "price": 500}
]

deliveries = [
    {"name": "National Post", "fees": 5},
    {"name": "DHL Express", "fees": 10}
]

payment_methods = ["Credit Card", "Skrill", "Bank Transfer"]


print("Available Products:")
for index, product in enumerate(products):
    print(f"{index}. {product['name']} - ${product['price']}")

while True:
    user_input = int(input("What do you want?"))
    try:
        user_input = int(user_input)
        if user_input >= 0 and user_input < len(products):
            break
        else:
            print("This product does not exist")
    except ValueError:
        print("please enter only numbers")

choosed_product = products[user_input]

print("Available dilivery methods:")
for index, method in enumerate(deliveries):
    print(f"{index}. {method['name']} - ${method['fees']}")



while True:
    user_method = int(input("Which dilivery method you prefer?"))
    try:
        user_input = int(user_input)
        if user_method >= 0 and user_method < len(payment_methods):
            break
        else:
            print("This method not exict")
    except ValueError:
        print("please enter only numbers")

choosed_method = deliveries[user_method]

total_price = choosed_method["fees"] + choosed_product["price"]
print(f"Your total is {total_price}")