import time

while True:
    start = 0.00

    num = int(input("Enter your number here: "))

    start = time.time()

    power = int(input("What power to do want to be raised upon the number: "))

    result = pow(num, power)
    print(f"\n{num} raised to the power of {power} is {result}\n")
    end = time.time()
    print(f"It took {end - start} seconds to print your answer!")