print("Wlcome to the custom Multiplication Table application by Muneer Alam\n")

while True:
    num = int(input("\nTable of what number do you want: "))
    mult = int(input("Upto what place do you want the table to be of: "))

    print(f"\nMultiplication table of {num} upto {mult}th place is\n\n")

    for i in range(1, mult+1):
        print(f"{num} x {i} = {num * i}")