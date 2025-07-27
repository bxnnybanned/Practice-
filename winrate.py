while True:
    try:
        hero = input("Enter your hero name: ")
        matches = int(input("Enter your matches: "))
        loss = int(input("Enter your lose/s: "))

        wins = matches - loss
        winrate = (wins / matches) * 100

        print("Your {} winrate is {:.1f}%".format(hero, winrate))

        while True:
            choice = input("Do you want to try again? (Y/N): ")
            if choice.upper() == 'Y':
                break
            elif choice.upper() == 'N':
                print("Goodbye!")
                exit(0)
            else:
                print("Input a valid choice (Y or N).")
                
    except ValueError:
        print("Input a number only.")
 