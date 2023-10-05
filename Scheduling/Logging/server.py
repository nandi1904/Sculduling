import functools
import time
import schedule

def print_elapsed_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_timestamp = time.time()
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed in %d seconds' % (func.__name__, time.time() - start_timestamp))
        return result

    return wrapper


@print_elapsed_time
def job():
    print('Hello World, Logs')
    time.sleep(5)

schedule.every().second.do(job)

schedule.run_all()