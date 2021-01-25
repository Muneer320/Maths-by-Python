while True:
    conversion = input("Welcome to the conversion table by Muneer\nPress the number corresponding to the conversion that you want to have.\n[1] Temperature Conversion\n[2] Length Conversion\n")

    if conversion == "1":
        temp = input("\n[1] Celsius to Fahrenheit\n[2] Celsius to Kelvin\n[3] Fahrenheit to Celsius\n[4] Fahrenheit to Kelvin\n[5] Kelvin to Celsius\n[6] Kelvin to Fahrenheit\n")

        if temp == "1":
            c = float(input("Enter the value for degree Celsius: "))
            result = (c * 9/5) + 32
            print(f"{c} degree Celsius in Fahrenheit is {result} degree Fahrenheit.")
        elif temp == "2":
            c = float(input("Enter the value for degree Celsius: "))
            print(f"{c} degree Celsius in Kelvin is {c + 273.15} degree Kelvin.")
        elif temp == "3":
            f = float(input("Enter the value for degree Fahrenheit: "))
            result = (f - 32) * 5/9
            print(f"{f} degree Fahrenheit in Celsius is {result} degree Celsius.")
        elif temp == "4":
            f = float(input("Enter the value for degree Fahrenheit: "))
            result = ((f - 32) * 5/9) - 273.15
            print(f"{f} degree Fahrenheit in Kelvin is {result} degree Kelvin.")
        elif temp == "5":
            f = float(input("Enter the value for degree Kelvin: "))
            print(f"{f} degree Kelvin in Celsius is {f - 273.15} degree Celsius.")
        elif temp == "6":
            f = float(input("Enter the value for degree Kelvin: "))
            print(f"{f} degree Kelvin in Fehrenheite is {(f - 273.15) * 9/5 + 32} degree Celsius.")
        else:
            print("Please write a valid number.")

    elif conversion == "2":
        unit = input("[1] Kilometre to Metre\n[2] Kilometre to Centimetre\n[3] Metre to Kilometre\n[4] Metre to Centimetre\n[5] Centimetre to Metre\n[6] Centimetre to Kilometre\n[7] Metre to Foot\n[8] Foot to Metre\n[9] Metre to Inch\n[10] Inch to meter\n[11] Metre to Yard\n[12] Yard to Metre\n[13] Metre to Mile\n[14] Mile to Yard\n[15] Metre to Nautical Mile\n[16] Nautical Mile to Metre")

        if unit == "1":
            km = float(input("Enter the value for Kilometre: "))
            print(f"{km} km in Metre is {km * 1000} Metres.")
        elif unit == "2":
            km = float(input("Enter the value for Kilometre: "))
            print(f"{km} km in centimetre is {km * 100000} centimetres.")
        elif unit == "3":
            m = float(input("Enter the value for Metre: "))
            print(f"{m} Metre in kilometre is {m / 1000} kilometres.")
        elif unit == "4":
            m = float(input("Enter the value for Metre: "))
            print(f"{m} Metre in centimetre is {m * 100} centimetres.")
        elif unit == "5":
            cm = float(input("Enter the value for centimetre: "))
            print(f"{cm} cm in Metre is {cm / 100} Metres.")
        elif unit == "6":
            cm = float(input("Enter the value for centimetre: "))
            print(f"{cm} cm in kilometre is {cm / 100000} kilometres.")
        elif unit == "7":
            m = float(input("Enter the value for Metre: "))
            print(f"{m} Metre in Foot is {m * 39.3701} Foot.")
        elif unit == "8":
            f = float(input("Enter the value for Foot: "))
            print(f"{f} Foot in Metre is {f / 39.3701} Metre.")
        elif unit == "9":
            m = float(input("Enter the value for Metre: "))
            print(f"{m} Metre in Inch is {m * 39.3701} Inch.")
        elif unit == "10":
            i = float(input("Enter the value for Inch: "))
            print(f"{i} Inch in Metre is {i / 39.3701} Metre.")
        elif unit == "11":
            m = float(input("Enter the value for Metre: "))
            print(f"{m} Metre in Yard is {m * 1.09361} Yard.")
        elif unit == "12":
            y = float(input("Enter the value for Yard: "))
            print(f"{y} Yard in Metre is {y / 1.09361} Metre.")
        elif unit == "13":
            m = float(input("Enter the value for Metre: "))
            print(f"{m} Metre in Mile is {m / 1609} Mile.")
        elif unit == "14":
            m = float(input("Enter the value for Mile: "))
            print(f"{m} Mile in Metre is {m * 1609} Metre.")
        elif unit == "15":
            m = float(input("Enter the value for Metre: "))
            print(f"{m} Mile in Nautical Mile is {m / 1852} Nautical Mile.")
        elif unit == "16":
            m = float(input("Enter the value for Nautical Mile: "))
            print(f"{m} Nautical Mile in Metre is {m / 1852} Metre.")
        else:
            print("Please write a valid number!")

    else:
        print("Please write a valid number.")