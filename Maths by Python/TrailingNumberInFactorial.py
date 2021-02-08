print("Number of Trailing Zeros Finder")

while True:
    num = int(input("Enter your number here: "))

    factorial = 1
    n = 5
    count = 0
    
    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)

    while (num // n != 0):
        count += int(num/n)
        n = n * 5
        
    print(f"The number of trailing zeroes in The factorial of {num} is {count}.")