import schedule
import time

def job():
    print("Scheduled task executed Forever!")

# Schedule the job to run every 15 seconds
schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
