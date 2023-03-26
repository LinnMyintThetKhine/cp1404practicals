MENU = """C - Convert Celsius to Fahrenheit
          F - Convert Fahrenheit to Celsius
          Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celius = float(input("Celsius>> "))
            fahrenheit = change_celsius_to_fahrenheit(celius)
            print(f"Result: {fahrenheit:.2f} F")


def change_celsius_to_fahrenheit(celius):
    return celius * 9.0 / 5 + 32

def change_fahrenheit_to_celsius(fahrenheit):
    return  5/9 * (fahrenheit - 32)

main()
