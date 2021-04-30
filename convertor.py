import requests
from tabulate import tabulate


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

        # function to do a simple cross multiplication between

    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))


# Currency_Convertor main code
def currency_conv():
    access_key = 'f10d160280cf22f605ce2ba95a9e57b1'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', access_key)
    c = Currency_convertor(url)
    print(" Country Currency List")
    d = [['Turkish lira', 'TRY'], ['Kuwati Dinar', 'KWD'], ['Bahraini Dinar', 'BHD'], ['Omani Rial', 'OMR'],
         ['Jordanian Dinar', 'JOD'],
         ['Gibraltar Pound', 'GIP'], ['Pound Sterling', 'GBP'], ['Cayman Island Dollars', 'KYD'], ['Euro', 'EUR'],
         ['United States Dollar', 'USD'],
         ['Swiss Franc', 'CHF'], ['Brunei Dollar', 'BND'], ['Canadian Dollar', 'CAD'], ['Australian Dollar', 'AUD'],
         ['Singapore Dollar', 'SGD'],
         ['Indian Rupees', 'INR'], ['Pakistani Rupess', 'PKR'], ['Nepalese Rupee', 'NPR'], ['Bangaldesh Taka', 'BDT']]
    print(tabulate(d, headers=["Country Currency", "Code"]))
    from_country = input("From Country (code): ")
    to_country = input("TO Country (code): ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)


# Length Convertor main code
def length_conv():
    d = [['cm', 'mm'], ['mm', 'cm'], ['m', 'cm'], ['cm', 'mm'], ['mm', 'm'], ['m', 'mm'], ['km', 'm'], ['m', 'km'],
         ['mm', 'km'], ['ft', 'cm'],
         ['ft', 'mm'], ['ft', 'inch'], ['inch', 'cm'], ['inch', 'mm']]

    print(tabulate(d, headers=["From Unit", "To Unit"]))
    unit1 = input('From Unit:  ')
    unit2 = input('To Unit: ')
    num1 = input('Enter the value: ')

    if unit1 == "cm" and unit2 == "m":
        ans = float(num1) / 100
        print(ans)
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1) / 10
        print(ans)
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1) * 100
        print(ans)
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1) * 10
        print(ans)
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1) / 1000
        print(ans)
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1) * 1000
        print(ans)
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1) * 1000
        print(ans)
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1) / 1000
        print(ans)
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1) / 1000000
        print(ans)
    elif unit1 == "ft" and unit2 == "cm":
        ans = float(num1) * 30.48
        print(ans)
    elif unit1 == "ft" and unit2 == "mm":
        ans = float(num1) * 304.8
        print(ans)
    elif unit1 == "ft" and unit2 == "inch":
        ans = float(num1) * 12
        print(ans)
    elif unit1 == "inch" and unit2 == "cm":
        ans = float(num1) * 2.54
        print(ans)
    elif unit1 == "inch" and unit2 == "mm":
        ans = float(num1) * 25.4
        print(ans)


# Temperature Convertor main code
def temp_conv():
    num1 = input('Enter the value: ')
    unit1 = input('Enter Far or Cel:')

    if unit1 == "far" or unit1 == "Far":
        ans = (float(num1) - 32) / 1.8
        print(num1, "F= ", ans, "*C")

    elif unit1 == "cel" or unit1 == "Cel":
        ans = (float(num1) * 1.8) + 32
        print(num1, "C= ", ans, "F")


# Weight Convertor main code

def weight_conv():
    # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'kg': 1000, 'hg': 100, 'dg': 10, 'g': 1, 'deg': 0.1, 'cg': 0.01, 'mg': 0.001}
    d = [['kg', 'Kilogram'], ['hg', 'hectogram'], ['dg', 'decagram'], ['g', 'gram'], ['deg', 'decigram'],
         ['cg', 'centigram'], ['mg', 'milligram']]
    print(tabulate(d, headers=["Unit", "Full form"]))

    # function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    amount = float(input("Enter the weight amount you want to convert :"))
    frmm = input("Enter the unit you want to convert from :")
    tto = input("Enter the unit you want to convert to :")

    ans = convert(amount, frmm, tto)
    print(ans)


# Area Convertor Main code

def area_conv():
    meterFactor = {'square meter': 1, 'square km': 1000000, 'square rood': 1011.7141056, 'square cm': 0.0001,
                   'square foot': 0.09290304,
                   'square inch': 0.00064516, 'square mile': 2589988.110336, 'milimeter': 0.000001,
                   'square rod': 25.29285264,
                   'square yard': 0.83612736, 'square township': 93239571.9721, 'square acre': 4046.8564224,
                   'square are': 100,
                   'square barn': 1e-28, 'square hectare': 10000, 'square homestead': 647497.027584}
    d = [['square meter'], ['[square km'], ['square rood'], ['square cm'], ['square foot'], ['square inch'],
         ['square mile'], ['milimeter'], ['square rod'], ['square yard'], ['square township'], ['square acre'],
         ['square are'], ['square barn'], ['square hectare'],
         ['square homestead']]

    print(tabulate(d, headers=["Unit"]))

    def convert(x, fromUnit, toUnit):
        result = (float(str(x)) * meterFactor[fromUnit]) / (meterFactor[toUnit])
        return result

    xt = float(input("Enter area amount :"))
    fromunit = input("Enter unit you want to convert from :")
    tounit = input("Enter unit you want to convert to :")

    ans = convert(xt, fromunit, tounit)
    print(ans)


# Driver code
if __name__ == "__main__":
    new_name = ''
    while new_name != 'quit':

        print("\n1. Currency Convertor\n"
              "2. Length Convertor\n"
              "3. Temperature Convertor\n"
              "4. Weight Convertor\n"
              "5. Area Convertor\n"
              "quit. Quit the Program\n")

        print("Enter Your choice : ")
        choice = input()
        if choice == '1':
            currency_conv()
        elif choice == '2':
            length_conv()
        elif choice == '3':
            temp_conv()
        elif choice == '4':
            weight_conv()
        elif choice == '5':
            area_conv()
        elif choice == 'quit':
            new_name = 'quit'
    print("*" * 50)
    print("Thank You")
