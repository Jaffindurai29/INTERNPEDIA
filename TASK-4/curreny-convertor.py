import requests

# Base URL for the exchange rate API (You can sign up at exchangerate-api.com and get your own API key)
API_URL = "https://v6.exchangerate-api.com/v6/your-api/latest/"

CURRENCY_CODES = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'JPY', 'CNY']

def fetch_exchange_rate(source_currency):
    try:
        response = requests.get(f"{API_URL}{source_currency}")
        response.raise_for_status()  
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates']
        else:
            print("Error fetching exchange rates. Please try again later.")
            return None
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None

def display_currency_list():
    print("\nAvailable Currencies:")
    for code in CURRENCY_CODES:
        print(f"- {code}")
def get_currency_input(prompt):
    while True:
        currency = input(prompt).upper()
        if currency in CURRENCY_CODES:
            return currency
        else:
            print(f"Invalid currency code. Please choose from the list below:")
            display_currency_list()

def get_conversion_amount():
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount > 0:
                return amount
            else:
                print("Amount must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def convert_currency(source_currency, target_currency, amount, rates):
    if target_currency in rates:
        converted_amount = amount * rates[target_currency]
        return converted_amount
    else:
        print(f"Conversion rate for {target_currency} not found.")
        return None

def currency_converter():
    while True:
        print("\n--- Currency Converter ---")
        display_currency_list()
        
        source_currency = get_currency_input("Enter the source currency: ")
        target_currency = get_currency_input("Enter the target currency: ")

        print(f"\nFetching live exchange rates for {source_currency}...")
        rates = fetch_exchange_rate(source_currency)
        if not rates:
            print("Failed to retrieve exchange rates. Please try again later.")
            continue

        amount = get_conversion_amount()

        converted_amount = convert_currency(source_currency, target_currency, amount, rates)
        if converted_amount:
            print(f"\n{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

        another_conversion = input("\nWould you like to perform another conversion? (y/n): ").lower()
        if another_conversion != 'y':
            print("Thank you for using the currency converter. Goodbye!")
            break

if __name__ == "__main__":
    currency_converter()
