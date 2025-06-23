templogic = False

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    
    while True:
        try:
            temp = input("enter a temperature and its unit example: (25 C) or (25 F): ")
            lowtemp = temp.lower()
            value = ""
            for char in lowtemp:
                if char.isdigit():
                    value = value + char

            value = int(value)

            if "c" in lowtemp and "f" in lowtemp:
                raise TypeError("invalid Temp Chars")
            
            elif value > 1000:
                raise ValueError("Invalid Temp Value")

            elif "c" in lowtemp:
                print("Celcius")
                templogic = True
                print("Temperature in Fahrenheit: ",round(celsius_to_fahrenheit(value)),"F")

            elif "f" in lowtemp:
                print("Fhrnh")
                templogic = False
                print("Temperature in Celsius: ",round(fahrenheit_to_celsius(value)),"C")

            else:
                print("be sure to Enter an Integer and Tempreture Char")
        except ValueError as VE:
            print(f"The type error is: {VE}")
        except TypeError as TE:
            print(f"The type error is: {TE}")
        except Exception as EXC:
            print(f"The type error is: {EXC}")






main()


