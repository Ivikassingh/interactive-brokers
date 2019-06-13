from ib_insync import *
import asyncio

ibc = IBC(  976, 
            gateway=False, 
            tradingMode='paper',
            userid='shree596', 
            password='finflock123', 
            twsPath='C:\Jts', 
            ibcPath='C:\IBC', 
            ibcIni='C:\IBC\config.ini'
        )

ibc.start()
IB.run()
