#To convert a date string in the format "dd/mm/yyyy" to a Julian date format "yyyyddd"

#    Parse the date string to extract the day, month, and year components.
#  Calculate the day of the year (ddd) using the given day and month.
 #   Concatenate the year (yyyy) and day of the year (ddd) to get the 7-digit integer in the Julian format.


def is_leap_year(year):
    # Helper function to check if a year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def date_to_julian(date_string):
    day, month, year = map(int, date_string.split('/'))
    
    # Define the number of days in each month for a non-leap year
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Update the number of days in February for a leap year
    if is_leap_year(year):
        days_in_month[2] = 29

    # Calculate the day of the year (ddd)
    day_of_year = sum(days_in_month[:month]) + day

    # Format the result as yyyyddd
    julian_date = year * 1000 + day_of_year
    
    return julian_date

# Example usage:
date_string = "20/07/2023"
julian_date = date_to_julian(date_string)
print(julian_date)  # Output: 2023201 (July 20, 2023 is the 201st day of the year)
