def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value
def GetFloat(low, high, string):
    while True:
        floatNumb = float(input(string))
        if floatNumb > low and floatNumb <= high:
            return floatNumb
        else:
            print("Number is invalid. Please enter a number between {low} and {high}")

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        print("=========================================================================")
        print()
        monthly_investment = GetFloat(0, 1000, "Enter Monthly Investment:\t")
        yearly_interest_rate = GetFloat(0, 15, "Enter yearly interest rate:\t")
        years = int(input("Enter number of years:\t\t"))

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
