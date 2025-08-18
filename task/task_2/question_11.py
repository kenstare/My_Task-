naira = float(input("Enter amount in Naira: "))
usd_rate = float(input("Enter exchange rate to US Dollars: "))
gbp_rate = float(input("Enter exchange rate to British Pounds: "))
usd = naira / usd_rate
gbp = naira / gbp_rate
print("\tCurrency Conversion Results:\n" +
      f"Naira:\t₦{naira:,.2f}\n" +
      f"USD:\t${usd:,.2f}\n" +
      f"GBP:\t£{gbp:,.2f}")
