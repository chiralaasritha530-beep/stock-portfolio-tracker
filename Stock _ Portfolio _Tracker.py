# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

total_value = 0

print("===== Stock Portfolio Tracker =====")

n = int(input("Enter the number of different stocks: "))

for i in range(n):
    stock = input("\nEnter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_value += investment

        print(f"{stock} Investment = ${investment}")
    else:
        print("Stock not available!")

print("\n==============================")
print(f"Total Investment Value = ${total_value}")
print("==============================")

# Save result to a text file
choice = input("\nDo you want to save the result? (yes/no): ").lower()

if choice == "yes":
    file = open("portfolio_report.txt", "w")
    file.write("Stock Portfolio Report\n")
    file.write("--------------------------\n")
    file.write(f"Total Investment Value = ${total_value}")
    file.close()
    print("Report saved as portfolio_report.txt")
else:
    print("Result not saved.")