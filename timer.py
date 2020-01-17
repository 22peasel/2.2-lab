#!/usr/bin/env python3

from datetime import datetime,  time, timedelta

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    current_time = start_time.strftime("%H:%M:%S")
    print("Start time:", current_time)
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    current_time2 = stop_time.strftime("%H:%M:%S")
    print("Stop time: ", current_time2)
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    
    if days > 0:
        print("Days:", days)
    print("Hours/minutes: " + str(hours) + ":" + str(minutes))
    print ("Seconds: " + str(seconds) + "." + str(microseconds))

if __name__ == "__main__":
    main()
