import calendar_generator;


print("="*30+"400 Year Calendar"+"="*30);
while True:
    
    choice =input("""
1. Print 400 Year Calendar
2. Print Specific Year's Calendar
3. Exit
input: """);
    
    if choice =='3' :
        exit();
    elif choice=='1' or choice=='2':    
        start_year=int(input("Enter Starting Year of the 400 year cycle : "));
        
        if choice =='1':
            calendar_generator.print_400_years_calendar(start_year);
        elif choice =='2':
            specific_year=int(input("Enter Specific Year in Range from next 400 Years (Starting Year: "+str(start_year)+"): "))
            
            if(specific_year > start_year and specific_year < start_year+400):
                calendar_generator.print_400_years_calendar(start_year,specific_year);
            else:
                print("Year Out of Range")
    else :
        print("Invalid Input");
   
    
    
    
    
    