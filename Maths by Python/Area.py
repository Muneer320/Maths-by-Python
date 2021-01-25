import time

while True:
    start = 0.00


    shape = input("Area of which shape do you want to find out:\n[1] Triangle\n[2] Square\n[3] Rectangle\n[4] Rhombus\n[5] Kite\n[6] Parallelogram\n[7] Trapezium\n[8] Irregular Quardrilateral\n[9] Regular Pentagon\n[10] Regular Hexagon\n[11] Regular Heptagon\n[12] Regular Octagon\n[13] Regular Nonagon\n[14] Regular Decagon\n[15] Regular n-gon\n")


    if shape == "1":
        formula = input("Which type of data are you giving...\n[1] Three sides and one angle.\n[2] One angle and the height perpendicular to it.\n(Just write 1 or 2)\n")

        if formula == "1":
            a = float(input('Enter the length of side: '))
            b = float(input('Enter the height: '))

            start = time.time()
            area = a * b * 0.5
            print('The area of the triangle is %0.2f' %area)
            end = time.time()
            print(f"It took {end - start} seconds to find and print your answer!\n")
            time.sleep(5)

        elif formula == "2":
            a = float(input('Enter first side: '))
            b = float(input('Enter second side: '))
            c = float(input('Enter third side: '))
            s = (a + b + c) / 2

            start = time.time()
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print('The area of the triangle is %0.2f' %area)
            end = time.time()
            print(f"It took {end - start} seconds to find and print your answer!\n")
            time.sleep(5)

        else:
            print("Please enter a valid number.\n")
            time.sleep(5)

    elif shape == "2":
        side = float(input("Enter the length of side: "))
        start = time.time()
        print(f"Area of the square of side {side} is {side*side}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    elif shape == "3":
        a = float(input("Enter the length: "))
        b = float(input("Enter the width: "))
        start = time.time()
        print(f"Area of the rectangle of length {a} and width {b} is {a*b}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    elif shape == "4":
        d1 = float(input("Enter diagonal 1: "))
        d2 = float(input("Enter diagonal 2: "))
        start = time.time()
        print(f"Area of the rhombus with diagonals {d1} and {d2} respectively is {(d1 * d2)/2}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    elif shape == "5":
        d1 = float(input("Enter diagonal 1: "))
        d2 = float(input("Enter diagonal 2: "))
        start = time.time()
        print(f"Area of the kite with diagonals {d1} and {d2} respectively is {(d1 * d2)/2}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)
    
    elif shape == "6":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        start = time.time()
        print(f"Area of parallelogram with base {base} and height {height} is {base * height}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    elif shape == "7":
        a = float(input("Enter the length of first parallel side: "))
        b = float(input("Enter the length of second parallel side: "))
        h = float(input("Enter the length between the parallel sides: "))
        start = time.time()
        print(f"Area of trapezium with parallel sides of length {a} and {b} respectively with height {h} is {h*(a+b)*0.5}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    elif shape == "8":
        d = float(input("Enter the length of diagonal: "))
        o1 = float(input("Enter the length of first offset: "))
        o2 = float(input("Enter the length of second offset: "))
        start = time.time()
        print(f"Area of quardrilateral with diagonal {d} and two of the offsets {o1} and {o2} respectively is {d*0.5*(o1+o2)}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    elif shape == "9":
        s = float(input("Enter the length of side: "))
        a = float(input("Enter the Apothem(height from middle of the polygon to the side at 90 degree): "))
        start = time.time()
        print(f"Area of the regular pentagon of side {s} and apothem {a} is {5*s*0.5*a}\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    elif shape == "10":
        s = float(input("Enter the length of side: "))
        a = float(input("Enter the Apothem(height from middle of the polygon to the side at 90 degree): "))
        start = time.time()
        print(f"Area of the regular hexagon of side {s} and apothem {a} is {6*s*0.5*a}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)
    
    elif shape == "11":
        s = float(input("Enter the length of side: "))
        a = float(input("Enter the Apothem(height from middle of the polygon to the side at 90 degree): "))
        start = time.time()
        print(f"Area of the regular heptagon of side {s} and apothem {a} is {7*s*0.5*a}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)
    
    elif shape == "12":
        s = float(input("Enter the length of side: "))
        a = float(input("Enter the Apothem(height from middle of the polygon to the side at 90 degree): "))
        start = time.time()
        print(f"Area of the regular octagon of side {s} and apothem {a} is {8*s*0.5*a}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)
    
    elif shape == "13":
        s = float(input("Enter the length of side: "))
        a = float(input("Enter the Apothem(height from middle of the polygon to the side at 90 degree): "))
        start = time.time()
        print(f"Area of the regular nonagon of side {s} and apothem {a} is {9*s*0.5*a}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)
    
    elif shape == "14":
        s = float(input("Enter the length of side: "))
        a = float(input("Enter the Apothem(height from middle of the polygon to the side at 90 degree): "))
        start = time.time()
        print(f"Area of the regular decagon of side {s} and apothem {a} is {s*5*a}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)
    
    elif shape == "15":
        n = float(input("Enter the number of side: "))
        s = float(input("Enter the length of side: "))
        a = float(input("Enter the Apothem(height from middle of the polygon to the side at 90 degree): "))
        start = time.time()
        print(f"Area of the regular decagon of side {s} and apothem {a} is {n*s*0.5*a}.\n")
        end = time.time()
        print(f"It took {end - start} seconds to find and print your answer!\n")
        time.sleep(5)

    else:
        print("Please enter a valid number!")
        time.sleep(5)