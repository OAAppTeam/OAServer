import Pyro.core
from PyQt4.QtCore import QCoreApplication
import sys, threading
from demoEngine import MainEngine
from eventEngine import EventEngine

def qtLoop():    
    daemon.requestLoop()
    

app = QCoreApplication(sys.argv)
me = MainEngine()
daemon=Pyro.core.Daemon(host='localhost',port=9000)

Pyro.core.initServer()

proxyOfMainEn = Pyro.core.ObjBase()
proxyOfMainEn.delegateTo(me)

proxyOfEventEn = Pyro.core.ObjBase()
proxyOfEventEn.delegateTo(me.ee)

daemon.connect(proxyOfMainEn, 'mainEn')
daemon.connect(proxyOfEventEn, 'eventEn')
t1 = threading.Thread(target=qtLoop,  name='loop')
t1.start()

app.exec_()

