#!/usr/bin/env python3

from datetime import datetime,  time, timedelta

def main():
    more = "y"
    while more.lower() == "y":
        print("Birthday Calculator")
        print()
        
        #name input
        name = input("Enter name: ")

        #birthday input
        bday = input("Enter birthday (MM/DD/YY): ")
        birthday = datetime.strptime(bday, '%m/%d/%y')
        current_day = datetime.today()
        temp = datetime(2020 , birthday.month , birthday.day)

        #calculations
        age = current_day - birthday 
        until_bday = temp - current_day
        
        

        #output
        print("Birthday: ", birthday.strftime("%B %d, %Y") )
        print("Today: ", current_day)
        print(name, "is", age.days // 365, "years old.")
        if temp > current_day:
            print(name,"'s birthday is in", until_bday)
        print()
        more = input("Continue? (y/n):")


if __name__ == "__main__":
    main()