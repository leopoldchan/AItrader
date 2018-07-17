import tushare as ts
import easytrader
import time 
from functools import reduce
import tushare as ts
import logging
import datetime

user = easytrader.use('ths')
user.connect(r'D:\同花顺软件\同花顺\xiadan.exe')

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  \
                    datefmt='%a, %d %b %Y %H:%M:%S',filename="AItrader.log",filemode='a')

T_9H = time.strftime("%H%M%S", time.strptime("09:30:00", "%H:%M:%S"))
T_11H = time.strftime("%H%M%S", time.strptime("11:30:10", "%H:%M:%S"))
T_13H = time.strftime("%H%M%S", time.strptime("13:00:00", "%H:%M:%S"))
T_1455H = time.strftime("%H%M%S", time.strptime("14:55:00", "%H:%M:%S"))
T_15H = time.strftime("%H%M%S", time.strptime("15:00:00", "%H:%M:%S"))


#检测昨日买的股票，破位卖股票，主卖
while True :
    time.sleep(1.5)
    df = ts.get_realtime_quotes('601360') #Single stock symbol
    df[['code','name','price','bid','ask','volume','amount','time']]
    TNOW = time.strftime("%H%M%S", time.strptime(str(df['time'])[5:13], "%H:%M:%S"))
    if (int(TNOW)<int(T_9H)):
        continue
    if (float(str(df['price'])[5:10])<27.61) : #27.61 
        break
    logging.info("realtime %s quotes:" % str(df))
    # print (float(str(df['price'])[5:10]))
    
print("exe sell process!")
# re = user.sell('601360', price=25.15, amount=300) # 27,89*0.9=25.10  跌停价卖
# logging.info("user.sell re: %s quotes:" % re)
# print(re)


#检测今日买的股票，收盘站回卖入点，主买
while True :
    time.sleep(1.5)
    df = ts.get_realtime_quotes('601360') #Single stock symbol
    df[['code','name','price','bid','ask','volume','amount','time']]
    logging.info("realtime %s quotes:" % str(df))
    TNOW = time.strftime("%H%M%S", time.strptime(str(df['time'])[5:13], "%H:%M:%S"))
    if (int(TNOW)<int(T_1455H)):  #等到收盘确认
        continue
    if (int(TNOW)>=int(T_15H)):  #收盘则结束程序
        exit()
    if (float(str(df['price'])[5:10])>=27.61) : #28.28  
        break
   

    # print (float(str(df['price'])[5:10]))

print("exe buy process!")
re = user.buy('601360', price=30.67, amount=300) # 27,89*1.10=30.679  跌停价卖
logging.info("user.buy re: %s quotes:" % re)
print(re) 