print("Welcome to my shop.")
answer = input("Would you like to buy something : ")
answer_upper = answer.upper()

gold = 500

if answer_upper == "YES":
    detail = input("Do you want to know the special ability of each item? ")
    detail_upper = detail.upper()
    item = input("What would you like to buy sword or dagger or a potion or a shield : ")
    item_upper = item.upper()
    if detail_upper == "YES":
        if item_upper == "SWORD":
            print("The sword grants his user strength and does double the damage to the enemy.")

        elif item_upper == "DAGGER":
            print("The dagger grants his user a special ability of dodging or reducing the damage at the same time "
                  "dealing more damage than normal")

        elif item_upper == "SHIELD":
            print("The shield grants his user ability of reducing the damage of the enemy")

        else:
            print("The potion heals the user when he is on a certain hp. 1 potion heals 20hp")

    else:
        pass

    if item_upper == "SWORD":
        print("The sword cost 100gold")
        agreed = input("Do you want it?")
        agreed_upper = agreed.upper()
        if agreed_upper == "YES":
            gold = gold - 100
            print("Now you have the sword in your inventory")
            print("Your remaining gold is", gold)
        else:
            exit()

    elif item_upper == "DAGGER":
        print("The dagger cost 100gold")
        print("Do you want it?")
        agreed = input()
        agreed_upper = agreed.upper()
        if agreed_upper == "YES":
            gold = gold - 100
            print("Now you have the dagger in your inventory")
            print("Your remaining gold is", gold)
        else:
            exit()

    elif item_upper == "POTION":
        print("The potion cost 50gold")
        agreed = input("Do you want it?")
        num = int(input("How many potions do you want?"))
        agreed_upper = agreed.upper()
        if agreed_upper == "YES" and 1 <= num <= 10:
            gold = gold - (50 * num)
            print("Now you have the", num, "potion in your inventory")
            print("Your remaining gold is", gold)
        else:
            exit()

    elif item_upper == "SHIELD":
        print("The shield cost 500gold")
        print("Do you want it?")
        agreed = input()
        agreed_upper = agreed.upper()
        if agreed_upper == "YES":
            gold = gold - 500
            print("Now you have the shield in your inventory")
            print("Your remaining gold is", gold)
        else:
            exit()

else:
    exit()


