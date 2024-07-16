"""
This program checks for leap years
"""

def check_leap():
    """
    Checks if the inputted year is a leap year
    """
    while True:
        try:
            year = int(input("Please enter a year: ").strip())
            break
        except ValueError:
            print("Only integers are accepted.")

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year!")
                print("Fun fact: leap years do not occur on years divisible by 100, except "\
                "for years divisible by 400.")
            else:
                print("This is NOT a leap year.")
                print("Fun fact: leap years do not occur on years divisible by 100, except "\
                "for years divisible by 400.")
        else:
            print("This is a leap year!")
    else:
        print("This is NOT a leap year.")

#starts program
check_leap()
    