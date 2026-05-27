# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

portfolio = {}
total_investment = 0

# Number of stocks user wants to enter
n = int(input("Enter number of stocks: "))

# Getting stock details from user
for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not available.")

# Calculating total investment
print("\nPortfolio Summary")
print("-------------------")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment

    print(f"{stock} : {qty} shares × ${price} = ${investment}")

print("-------------------")
print("Total Investment Value = $", total_investment)

# Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")

    file.write("Portfolio Summary\n")
    file.write("-------------------\n")

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = price * qty

        file.write(f"{stock} : {qty} shares × ${price} = ${investment}\n")

    file.write("-------------------\n")
    file.write(f"Total Investment Value = ${total_investment}")

    file.close()

    print("Result saved in portfolio.txt")