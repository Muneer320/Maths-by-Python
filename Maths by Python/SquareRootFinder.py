import time

while True:
    start = 0.00

    num = float(input("Please write your desired number here: ")) 

    start = time.time()

    num_sqrt = num ** 0.5
    print('\nThe square root of %0.3f is %0.3f'%(num ,num_sqrt))

    end = time.time()
    print(f"\nIt took {end - start} seconds to print your answer!\n")