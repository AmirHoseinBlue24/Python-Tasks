def calculate_inflation(before_price, now_price):
    inflation_rate = ((now_price - before_price) / before_price) * 100
    next_year_price = now_price + (inflation_rate * now_price / 100)
    return inflation_rate, next_year_price

before_price = float(input("Enter last year's price: "))
now_price = float(input("Enter this year's price: "))

inflation_rate, next_year_price = calculate_inflation(before_price, now_price)

print("Inflation rate:", round(inflation_rate, 2), "%")
print("Predicted price for next year:", round(next_year_price, 2))
