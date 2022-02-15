def main():

    print("===========================================================================")
    print()
    print("Welcome to the Baseball batting stats calculator!")
    print()
    player_name = input("Enter the players name:\t")
    print()
    bat_stat = int(input("For just batting average enter 1. For more stats enter 2.\t"))
    print()
    if bat_stat == 1:
        bat_ab1 = float(input("Enter the number of at bats the player has had.\t\t"))
        bat_hit1 = float(input("Enter the number of hits the player has.\t\t"))
        bat_avg1 = bat_hit1 / bat_ab1
        bat_avg1 = round(bat_avg1, 3)
        print(player_name," has a batting average of: ", bat_avg1)
        print("===========================================================================")
        restart = input("Would you like to start over? Type yes or no.\t") .lower()
        if restart == "yes":
            main()
        else:
            print("See you later!")
            quit()
    if bat_stat == 2:
        bat_pa = int(input("Enter the number of plate appearances has the player had.\t"))
        bat_walk = int(input("Enter the amount of times the player has been walked/HBP.\t"))
        bat_sac = int(input("Enter the amount of times the player has performed a Sacrifice play (SF/SAC). "))
        bat_sing = int(input("Enter the amount of singles the player has.\t"))
        bat_doub = int(input("Enter the amount of doubles the player has.\t"))
        bat_trip = int(input("Enter the amount of tripples the player has.\t"))
        bat_hr = int(input("Enter the amount of home runs the player has.\t"))
        onbase = bat_sing + bat_doub + bat_trip + bat_hr + bat_walk - bat_sac
        bat_obp = onbase / bat_pa
        bat_obp = round(bat_obp, 3)
        bat_hit2 = bat_sing + bat_doub + bat_trip + bat_hr
        atbat = bat_pa - bat_walk
        bat_avg2 = bat_hit2 / atbat
        bat_avg2 = round(bat_avg2, 3)
        bat_bases = bat_sing + (bat_doub * 2) + (bat_trip * 3) + (bat_hr * 4)
        bat_slg = bat_bases / atbat
        bat_slg = round(bat_slg, 3)
        bat_ops = bat_obp + bat_slg
        bat_ops =  round(bat_ops, 3)
        print()
        name = player_name + "'s batting stats are as shown:"
        print(name)
        print()
        print("On Base Percentage:\t", bat_obp)
        print("Batting Average:\t", bat_avg2)
        print("Slugging Percentage:\t", bat_slg)
        print("On base + Slugging (OPS):", bat_ops)
        print()
        print("===========================================================================")
        restart = input("Would you like to start over? Type yes or no.\t") .lower()
        if restart == "yes":
            main()
        else:
            print("See you later!")
            quit()
    else:
        print("Error. Please try again")
        main()
main()
