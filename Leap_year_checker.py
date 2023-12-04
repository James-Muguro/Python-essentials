# ## Leap Year Checker

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter a year to check if it's a leap year: "))
        if year >= 0:
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print("Please enter a valid year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()