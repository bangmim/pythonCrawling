print("Hello World~!!")

import time
import datetime

wtoday=time.strftime('%d', time.localtime(time.time()))
today=datetime.date.today()
yesterday=today-datetime.timedelta(1)

# datetime.timedelta('num') : num만큼의 일자
# datetime.timedelta(2) : 2days
# datetime.timedelta(1) : 1days

print("wtoday : ",wtoday)   # 오늘 day를 숫자만 표시한다
print("today : ",today)     # 오늘 day가 출력된다. (YYYY-MM-dd 형식)
print("yesterday : ",yesterday)

print(datetime.timedelta(2))

