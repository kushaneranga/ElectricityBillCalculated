print("**Electric bill calculation**")
units = float(input("Number of Units (KWH): "))
if units <= 50:
    amount = units * 5
elif 50 < units <= 150:
    amount = (50 * 5) + (units - 150) * 7
elif units > 150:
    amount = (50 * 5) + (150 - 50) * 7 + (units - 150) * 10
TAX = float(amount) * 20 / 100
print("Your bill Rs: ", amount + TAX)
