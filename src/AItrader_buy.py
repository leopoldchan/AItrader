import tushare as ts
import easytrader
import time 
from functools import reduce
import tushare as ts
import logging
import datetime

# user = easytrader.use('ths')
# user.connect(r'D:\同花顺软件\同花顺\xiadan.exe')

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  \
                    datefmt='%a, %d %b %Y %H:%M:%S',filename="AItrader.log",filemode='a')

T_9H = time.strftime("%H%M%S", time.strptime("09:30:00", "%H:%M:%S"))
T_11H = time.strftime("%H%M%S", time.strptime("11:30:10", "%H:%M:%S"))
T_13H = time.strftime("%H%M%S", time.strptime("13:00:00", "%H:%M:%S"))
T_15H = time.strftime("%H%M%S", time.strptime("15:00:00", "%H:%M:%S"))
i=0
while True :
    i = i+1
    time.sleep(1.5)
    df = ts.get_realtime_quotes('601360') #Single stock symbol
    df[['code','name','price','bid','ask','volume','amount','time']]
    TNOW = time.strftime("%H%M%S", time.strptime(str(df['time'])[5:13], "%H:%M:%S"))
    if (int(TNOW)>=int(T_15H)):
        print("time is after 15:00")
        exit()
    if((float(str(df['price'])[5:10])>=28.08) and (float(str(df['price'])[5:11])<=28.11)): #28.28  
        break
    logging.info("realtime %d quotes:" % i)
    logging.info("realtime %s quotes:" % str(df))
    # print (float(str(df['price'])[5:10]))
    
print("exe buy process!")
# re = user.buy('601360', price=30.52, amount=300) # 27,75*1.10=30.525  涨停价买
# logging.info("user.buy re: %s quotes:" % re)
# print(re)

# re = user.sell('000735', price=12.00, amount=100)