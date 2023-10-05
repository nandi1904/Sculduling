# Schedule multiple tasks 

import schedule
import time

def task1():
    print("Task 1 executed!")

def task2():
    print("Task 2 executed!")

def task3():
    print("Task 3 executed!")

# Schedule Task 1 to run every 5 seconds
schedule.every(5).seconds.do(task1)

# Schedule Task 2 to run every 10 seconds
schedule.every(20).seconds.do(task2)

# Schedule Task 3 to run every 30 seconds
schedule.every(50).seconds.do(task3)

while True:
    schedule.run_pending()
    time.sleep(1)
