"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    print(score_review(score))

def score_review(score):
    if score > 100:
        return "Invalid score"
    elif 90 > score > 50:
        return "Passable"
    elif 100 >= score >= 90:
        return "Excellent"
    else:
        return "Bad"

main()