from schedule import every, repeat, run_pending
import time

@repeat(every(1).minutes)
def job():
    print("I am doing job")

while True:
    run_pending()
    time.sleep(1)