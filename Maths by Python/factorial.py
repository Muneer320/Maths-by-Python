import time

while True:
    start = 0.00

    num = int(input("Enter your number here: "))

    start = time.time()

    factorial = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
    end = time.time()
    print(f"It took {end - start} seconds to print your answer!")