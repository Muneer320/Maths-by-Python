while True:
    num = int(input("Please write your number here: "))

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(f"\n{num} is not a prime number\n")
                print(f"{i} times {num//i} is {num}")
                break
        else:
            print(f"\n{num} is a prime number")
            
    else:
        print(f"\n{num} is not a prime number\n")