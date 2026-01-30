
unit: str = input("Is this temperature in Celsius or Fahrenheit (C/F): ").capitalize()

if unit == "C" or unit == "F":
    temp: float = float(input("Enter the temperature: "))

    if unit == "C":
        summary: float = (9 * temp) / 5 + 32
        print(f"{temp} degree is {round(summary, 2)} Fahrenheit ")
    elif unit == "F":
        summary: float = (temp - 32) * 5 / 9
        print(f"{temp} Fahrenheit is {round(summary, 2)} degree")

else:
    print(f"{unit} is an invalid unit!") 

