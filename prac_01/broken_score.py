"""
CP1404/CP5632 - Practical
Program calculates if your score is Excellent, Passable, Bad or Invalid
"""
"""Kevin Hinds"""
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")


