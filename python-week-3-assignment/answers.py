def calculate_discount(price, discount_percent):
    if discount_percent > 0:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    price = float(input("Enter Price Here: "))
    discount_percent = float(input("Enter Discount in Percentage Here: "))

    if price < 0 or discount_percent < 0:
        print("Price and discount percentage must be positive numbers.")
    else:
        final_price = calculate_discount(price, discount_percent)
        print(f"Final Price: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")