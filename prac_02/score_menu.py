MENU = """(G)et a valid score (must be 0-100 inclusive)
          (P)rint result (copy or import your function to determine the result from score.py)
          (S)how stars (this should print as many stars as the score)
          (Q)uit"""

def main():
    score = input("your score : ")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            result = get_valid_score
            print(result)
        elif choice == "P":
            celsius = print_result(score)
            print(result)
        elif choice == "S":
            result = show_star(score)
            print(result)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_valid_score():
    while True:
        try:
            score = int(input("Enter a score (0-100 inclusive): "))
            if score < 0 or score > 100:
                raise ValueError
            return score
        except ValueError:
            print("Invalid score. Please try again.")

def print_result(score):
    while score != 0:
        if score > 100:
            print("Invalid score")
        elif 90 > score > 50:
            print("Passable")
        elif 100 >= score >= 90:
            print("Excellent")
        else:
            print("Bad")
def show_star(score):
    result = "*" * score
    print(result)
main()






