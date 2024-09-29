
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import time


class Manager:

    def __init__(self , symbol ) -> None:
        self.authentication()
        self.symbol = symbol

        
    def authentication(self):
                if not mt5.initialize():
                     print('this is error code', mt5.last_error())
                     quit()
         
    def sell_order_w(self , symbol ,lot ,comment ):
     
         price = mt5.symbol_info_tick(symbol).ask
         point = mt5.symbol_info(symbol).point

         request = {
             
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "deviation": 10,
            "magic": 0,
            "comment": comment,
            "type_filling": 1,
            "type_time": mt5.ORDER_TIME_GTC}
         result = mt5.order_send(request)

         return result[2]

    def buy_order_w(self , symbol , lot , comment ):
         price = mt5.symbol_info_tick(symbol).ask

         request = {
             
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "deviation": 10,
            "magic": 0,
            "comment": comment,
            "type_filling": 1,
            "type_time": mt5.ORDER_TIME_GTC}
         
         result = mt5.order_send(request)
         return result[2]
    

    def manage(self):
          positions=mt5.positions_get(symbol= self.symbol)
          if len(positions) ==0:
                
                self.buy_order_w('EURUSD', 1.0 , 'buy eurusd')
                self.sell_order_w('GBPUSD', 1.0 , 'sell gbpusd')
                self.sell_order_w('EURGBP', 1.0 , 'sell eurgbp')