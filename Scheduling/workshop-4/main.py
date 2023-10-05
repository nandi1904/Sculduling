import schedule
import time
import datetime

def morning_task():
    print("Morning task executed at", datetime.datetime.now())

def afternoon_task():
    print("Afternoon task executed at", datetime.datetime.now())

def evening_task():
    print("Evening task executed at", datetime.datetime.now())

# Schedule a morning task at 8:00 AM
schedule.every().day.at("08:00").do(morning_task)

# Schedule an afternoon task at 1:00 PM
schedule.every().day.at("2:00").do(afternoon_task)

# Schedule an evening task at 7:00 PM
schedule.every().day.at("19:00").do(evening_task)

while True:
    schedule.run_pending()
    time.sleep(1)
