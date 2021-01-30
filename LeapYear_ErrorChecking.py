def isLeapYear(year):
    if  year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
               return True
            else:
                return False
    
yearString = input("Enter the year: ")

try:
    year = int(yearString)
    
except ValueError:
    print("Input was not an valid year number")

else:

    try:
        if year <= 1:
            print("Input year was invalid (zero or negative)")
            raise ValueError
        
    except ValueError:
        pass

    else:
        outString = " is a leap year" if isLeapYear(year) else " is not a leap year"
        print(str(year) + outString)
        

