def calculate_total_price(product_price,sales_tax_rate):
    # print(product_price)
    # print(sales_tax_rate)
    try:
        if product_price < 0:
            raise ValueError("this is a negative")
        total_price = (1 + sales_tax_rate) * product_price
    except ValueError as e:
        print(f"value error, try again") # type a formatted string with the value error message
    else: 
        return total_price

price = calculate_total_price(20, 0.5)
print(price)