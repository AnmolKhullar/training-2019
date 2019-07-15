# Min in a year

year = int(input("Enter Year: "))

if ((year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)):
    print("Number of min (Leap): ", 366 * 24 * 60, "min")

else:
    print("Number of min (Non-Leap): ", 365 * 24 * 60, "min")
