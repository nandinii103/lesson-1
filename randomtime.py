import random
import time
from datetime import datetime

def generate(nandinii , nandiniipart2):
    startTime = time.mktime(time.strptime(nandinii , "%Y - %m - %d"))

    endtime = time.mktime(time.strptime(nandiniipart2 , "%Y - %m - %d"))
    randomTime = random.uniform(startTime , endtime)

    return datetime.fromtimestamp(randomTime)
print(generate("2026 - 01 - 01" , "2028 - 06 - 08"))
    