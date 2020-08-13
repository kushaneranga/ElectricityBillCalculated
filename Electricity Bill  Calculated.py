print("***Electric bill calculation***")
units = float(input("Number of Units (KWH): "))
if units <= 30:
    amount = units * 7.85
    fixed_cost = 30
elif 30 < units <= 60:
    amount = (30 * 7.85) + (units - 30) * 7.85
    fixed_cost = 60
elif 60 < units <= 90:
    amount = (30 * 7.85) + (60 - 30) * 7.85 + (units - 60) * 10
    fixed_cost = 90
elif 90 < units <= 120:
    amount = (30 * 7.85) + (60 - 30) * 7.85 + (90 - 60) * 10 + (units - 90) * 27.75
    fixed_cost = 480
elif units > 120:
    amount = (30 * 7.85) + (60 - 30) * 7.85 + (90 - 60) * 10 + (120 - 90) * 27.75 + (units - 120) * 32
    fixed_cost = 480
Full_Amount = amount + fixed_cost
Tax = Full_Amount * 15 / 100  # 15% Tax
Pay_Amount = Full_Amount + Tax
print("Your bill Rs: ", Pay_Amount, "/=")
