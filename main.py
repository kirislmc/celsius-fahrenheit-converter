
unit: str = input("Is this temperature in Celsius or Fahrenheit (C/F): ").capitalize()

if unit == "C":
    temp: float = float(input("Enter the temperature: "))
    summary = (9 * temp) / 5 + 32
    print(f"{temp} degree is {round(summary, 2)} Fahrenheit ")

elif unit == "F":
    temp: float = float(input("Enter the temperature: "))
    summary = (temp - 32) * 5 / 9
    print(f"{temp} Fahrenheit is {round(summary, 2)} degree")

else:
    print(f"{unit} is an invalid unit!")