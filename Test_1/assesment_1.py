''' Create a method which returns interval date by the following condition
Give start and end date (both inclusive) in the ‘YYYYMMDD’ format (ex. 20181231 is 31st Dec
2018), output list of dates that satisfy exactly one of the following conditions. The output
should be in chronological order. One date per line. Input dates belong between the year 1900
to 2100.
1. The day is the 4th Saturday of the month.
2. The day is Saturday and the date is multiple of 5.

Example:
Input dates
• Start date: 20180728
• End date: 20180927

Output:
• 20180728
• 20180915
• 20180922

Explanation:
20180728 4th Saturday of July (28th July 2018) 20180825 Not in the solution as it satisfies both
the conditions. 20180915 The date is multiple of 5 and it is a Saturday. 20180922 4th Saturday
of September.
'''


from datetime import datetime, timedelta, date

def fourth_saturday(input_date):
    '''
    This function returns the fourth saturday of the month
    based on the input date fed to it.
    '''
    year, month = input_date.year, input_date.month
    first_day = date(year, month, 1)

    if first_day.weekday() == 0:                                        # Since Monday = 0
        date_sat =  (first_day + timedelta(26)).strftime("%Y%m%d")
    elif first_day.weekday() == 1:                                      # Since Tuesday = 1
        date_sat =  (first_day + timedelta(25)).strftime("%Y%m%d")
    elif first_day.weekday() == 2:                                      # Since Wednesday = 2
        date_sat =  (first_day + timedelta(24)).strftime("%Y%m%d")
    elif first_day.weekday() == 3:                                      # Since Thursday = 3
        date_sat =  (first_day + timedelta(23)).strftime("%Y%m%d")
    elif first_day.weekday() == 4:                                      # Since Friday = 4
        date_sat =  (first_day + timedelta(22)).strftime("%Y%m%d")
    elif first_day.weekday() == 5:                                      # Since Saturday = 5
        date_sat =  (first_day + timedelta(21)).strftime("%Y%m%d")
    elif first_day.weekday() == 6:                                      # Since Sunday = 6
        date_sat =  (first_day + timedelta(27)).strftime("%Y%m%d")
    return date_sat

if __name__ == "__main__":

    start_date = datetime.strptime((input()), '%Y%m%d')
    end_date = datetime.strptime((input()), '%Y%m%d')
    difference_between_dates = end_date - start_date
    for i in range(difference_between_dates.days + 1):
        the_date = start_date + timedelta(days=i)
        if the_date.weekday() == 5:
            if int(the_date.strftime("%d"))%5 == 0 :
                if the_date.strftime("%Y%m%d") == fourth_saturday(the_date):
                    pass
                else:
                    print(the_date.strftime("%Y%m%d"))

            elif the_date.strftime("%Y%m%d") == fourth_saturday(the_date):
                print(the_date.strftime("%Y%m%d"))
