#ex1
import datetime as dt
now = dt.datetime.now()
ans = now - dt.timedelta(5)
print(ans)
#ex2
import datetime as dt
now = dt.datetime.now()
yest = now - dt.timedelta(1)
tomor = now + dt.timedelta(1)
print("Yesterday was ", yest)
print("Today is ", now)
print("Tomorrow will be ", tomor)
#ex3
import datetime as dt
now = dt.datetime.now().replace(microsecond=0)
print(now)
#ex4
from datetime import datetime

date1 = datetime(2023, 5, 15, 12, 30, 0)  
date2 = datetime(2023, 5, 10, 8, 45, 0)   
minus = date1 - date2
diff = minus.total_seconds()
print(diff)