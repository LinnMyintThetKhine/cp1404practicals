menu = """ H: hello 
G: good bye
Q: Finished"""
name = input("Enter Name : ")
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice =="G":
        print("Goodbye", name)
    else:
        print("Invalid option")
    print(menu)
    choice = input(">>> ").upper()
print("Finished")