#1
name = input("Please enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

print("Name saved to file.")
# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)
# 3

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
result = number1+ number2
print(result)

# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)