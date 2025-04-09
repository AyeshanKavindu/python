def get_price_with_vat(price):
    return price + (price * 20 / 100)

price_with_vat = get_price_with_vat(100)

print(f"Price with vat: {price_with_vat}")