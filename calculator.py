while True:
    try:
        num1 = float(input("Enter a number: "))

        while True:
            op = input("Enter an operator (+, -, *, /): ")
            if op in ['+', '-', '*', '/']:
                break
            else:
                print("Invalid operator! Please enter one of (+, -, *, /).")

        num2 = float(input("Enter another number: "))

        while True:
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Invalid! Division by zero.")
                    break
                result = num1 / num2

            print("Result = {:.2f}".format(result))
            break

        while True:
            again = input("Do you want to try again? (y/n): ")
            if again != 'y':
                print("Goodbye!")
                exit()
            break

    except ValueError:
        print("Enter numbers only.")
