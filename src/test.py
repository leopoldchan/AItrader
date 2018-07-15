import tushare as ts
import easytrader

# df=ts.get_hist_data('600848') #一次性获取全部数据
# print(df[['ma10']])

import tushare as ts

user = easytrader.use('ths')
user.connect(r'D:\同花顺软件\同花顺\xiadan.exe')

while True :
    time.sleep(1)
    df = ts.get_realtime_quotes('601360') #Single stock symbol
    df[['code','name','price','bid','ask','volume','amount','time']]
    print(df)




str=user.balance
print(str)

re = user.sell('000735', price=12.00, amount=100)
print(re)

# re = user.buy('600460', price=12.39, amount=100)
# print(re)

# re = user.cancel_entrust('buy/sell 27')
# print(re)

