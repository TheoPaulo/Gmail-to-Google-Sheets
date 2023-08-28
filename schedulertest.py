import schedule
import os
import time as tm
from datetime import time, timedelta, datetime
def do_nothing():
    print("soumil shah")

def job():
    print("Subscribe to NeuralNine!")

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)
    if os.path.exists("TestFile"):
        os.remove("TestFile")
    else:
        print("bruh")