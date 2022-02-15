def main():

    print("Welcome to the Miles per Gallon calculator!")
    print()
    miles_driven= float(input("How many miles have been driven?\t\t"))
    if miles_driven > 0:
        gallons_used= float(input("How many gallons of gas have been used?\t\t"))
        if gallons_used > 0:
            mpg = miles_driven / gallons_used
            mpg = round(mpg, 1)
            print("Your vehicles Miles per Gallon:\t",mpg) 
        else:
            print ("Error. Gallons used must be more than 0.")
    else:
        print("Error. Miles driven must be more than 0.")
    restart = input("Would you like to try again? Please type yes or no.\t\t") .lower()
    if restart == "yes":
        main()
    else:
        print("Goodbye!")
        exit()
main()
