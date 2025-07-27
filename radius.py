while True:
    try:
        c = float(input("Enter the value of circumference: "))
        
        r = c / (2 * 3.14)
        
        print("The radius of a circle is {:.2f}". format(r))
        
        while True:
            choice = input("Do you want to try again? (Y/N): ")
            if choice.upper() == 'Y':
                break
            elif choice.upper() == 'N':
                exit(0)
                break
            else:
                print("Invalid choices.")
                
    except ValueError:
        print("Enter a number only.")                