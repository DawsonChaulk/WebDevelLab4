def main():

    print("======================================================")
    print()
    print("Area and Perimeter Calculator!")
    print()
    len = float(input("Please enter the length:\t"))
    wid = float(input("Please enter the width:\t\t"))
    print ()
    Area = len * wid
    Per = (2* len) + (2 * wid)
    print("Area = ", Area)
    print("Perimeter = ", Per)
    print()
    print("======================================================")
    restart = input("Would you like to try again?\t")
    if restart == "yes":
        main()
    else:
        print("See you later!")
        quit()

main()
