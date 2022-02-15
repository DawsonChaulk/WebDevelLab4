def lines():
    print("=====================================================================")


def menui():
    print("                     Batting Average Calculator                      ")
    print("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit program")
def menf():
    menop = int(input("Menu Option:\t"))
    return menop
def calcBA(hit, ab):

    Hits = int(input(hit))
    if Hits <= 0:
        print("Error! Player must have more than 0 hits! Try again")
    abs = int(input(ab))
    if abs <= 0:
        print("Error! Player must have more than 0 at bats! Try again")
    BA = float(Hits/abs)
    BA = round(BA, 3)
    print("The players batting average is:\t\t", BA)
    print()

lines()
menui()
lines()
def main():
    while True:
        menop = menf()
        if menop == 1:
            print("Calculate batting average... ")
            calcBA("Enter Number of Hits the player has:\t", "Enter Number of at bats the player has had:\t")
        elif menop == 2:
            print("Goodbye!")
            lines()
            quit()
        elif menop != 1 and menop != 2:
            print("Incorrect input! Please Try Again!")


main()
