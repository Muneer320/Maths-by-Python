while True:
    num1 = int(input("\n\nEnter first number\n"))
    num2 = int(input("\nEnter second number\n"))

    if num2>num1:
        mn = num1
    else:
        mn = num2

    for i in range(1, mn+1):
        if num1%i==0 and num2%i==0:
            hcf = i
    print(f"\nThe HCF of these two numbers is {hcf}")