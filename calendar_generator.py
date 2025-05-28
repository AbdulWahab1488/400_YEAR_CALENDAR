import calendar

def print_400_years_calendar(start_year=2001,specific_year=-1):
    if(specific_year==-1):
        # Ensure start year is the beginning of a 400-year cycle
        if (start_year - 1) % 400 != 0:
            print("Start year should be the beginning of a 400-year cycle (like 1601, 2001, etc.)")
            return

        for year in range(start_year, start_year + 400):
            print(f"\n{'='*30}\nYEAR: {year}\n{'='*30}")
            for month in range(1, 13):
                print(f"\n{calendar.month_name[month]} {year}")
                print(calendar.month(year, month))
    else:
        
        print(f"\n{'='*30}\nYEAR: {specific_year}\n{'='*30}")
        for month in range(1, 13):
            print(f"\n{calendar.month_name[month]} {specific_year}")
            print(calendar.month(specific_year, month))
        
    

