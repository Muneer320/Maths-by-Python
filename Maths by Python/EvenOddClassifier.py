while True:
    num = input("Number => ")

    if num == int:
        pass
    else:
        print("Please write a valid number.")
        break

    if num % 2 == 0:
        print("The number is Even")
        print(f"{num} / 2 = {num/2}\nWhich is a non-decimal number, hence it is an even number.")

    elif num % 2 != 0:
        print("The number is Odd")
        print(f"{num} / 2 = {num/2}\nWhich is a decimal number, hence it is an odd number.")

    else:
        print("Please write a no decimal numeric value")