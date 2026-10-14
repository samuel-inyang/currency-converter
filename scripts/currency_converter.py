# Currency Conversion Program for Travel Agent
# Author: SAMUEL ETONG INYANG

EXCHANGE_RATES = {
    "USD": 1.26,   
    "EUR": 1.15, 
    "BRL": 6.45,   
    "JPY": 182.30, 
    "TRY": 41.70   
}

def  Transaction_Fee(GBP):
    if GBP <= 299.99:
        fee_rate = 0.035
    elif GBP >= 300 and GBP <= 749.99:
        fee_rate = 0.03
    elif GBP >= 750 and GBP <= 999.99:
        fee_rate = 0.025
    elif GBP >= 1000 and GBP <= 1999.99:
        fee_rate = 0.02
    elif GBP >= 2000 and GBP <= 2500:
        fee_rate = 0.015
    elif GBP > 2500:
        print("Limit exceeded. Maximum amount is £2500.")
    return GBP * fee_rate

def Convert_Currency(GBP, Currency):
    """Converts GBP to the selected currency using the exchange rate."""
    rate = EXCHANGE_RATES.get(Currency)
    return GBP * rate

def display_results(Currency, converted_amount, fee, discount, total_cost):
    print("\n--- Transaction Summary ---")
    print(f"Currency selected: {Currency}")
    print(f"Amount received in {Currency}: {converted_amount:.2f}")
    print(f"Transaction fee (GBP): £{fee:.2f}")
    print(f"Discount applied (GBP): £{discount:.2f}")
    print(f"Total cost in GBP: £{total_cost:.2f}")
    print("-----------------------------")

def main():
    print("Welcome to the Travel Agent Currency Converter!\n")

    # total amount in GBP
    while True:
        try:
            GBP = float(input("Enter the amount in GBP to convert: £"))
            if GBP <= 0:
                print("Please enter a positive amount.")
                continue
            elif GBP > 2500:
                print("Limit exceeded. Maximum amount is £2500.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Currency election
    print("\nAvailable currencies: USD, EUR, BRL, JPY, TRY")
    while True:
        Currency = input("Enter the target currency: ").upper()
        if Currency in EXCHANGE_RATES:
            break
        else:
            print("Invalid currency. Please choose from USD, EUR, BRL, JPY, TRY.")

    converted_amount = Convert_Currency(GBP, Currency)

    # Transaction fee
    fee = Transaction_Fee(GBP)

    # Total cost before discount
    total_cost = GBP + fee

    # Ask if customer is staff
    is_staff = input("Is the customer a staff member? (yes/no): ").strip().lower()
    discount = 0
    if is_staff in ["yes", "y"]:
        discount = 0.05 * total_cost
        total_cost -= discount

    # Display results
    display_results(Currency, converted_amount, fee, discount, total_cost)

    print("\nThank you for using the Travel Agent Currency Converter!")

# Run the program
main()
