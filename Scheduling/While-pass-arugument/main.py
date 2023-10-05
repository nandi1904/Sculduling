import schedule

def greet(name):
    print('Hello', name)

schedule.every(2).seconds.do(greet, name='Aishu')
schedule.every(4).seconds.do(greet, name='Babu')

from schedule import every, repeat

@repeat(every().second, "World")
@repeat(every().day, "Mars")
def hello(planet):
    print("Hello", planet)

while True:
    schedule.run_pending()
