MENU = """C - Convert Celsius to Fahrenheit
          F - Convert Fahrenheit to Celsius
          Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            celsius = float(input("Celsius>> "))
            fahrenheit = change_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit>> "))
            celsius = change_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
def change_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def change_fahrenheit_to_celsius(fahrenheit):
    return  5/9 * (fahrenheit - 32)

main()

