import threading 
import time


class NS_APP:
    def print(n, sym):
        print(sym + str(n)) 


def func1():
    NS_APP.print(threading.main_thread(), 'Main Thread object: ')

    threading.current_thread().name = "January"
    NS_APP.print(threading.current_thread(), 'Thread Object: ')
    NS_APP.print(threading.get_ident(), 'Thread Ident: ')
    NS_APP.print(threading.get_native_id(), 'Thread Native Id: ')
    NS_APP.print(threading.current_thread().name, 'Thread Name: ')
    time.sleep(5)
    
    print("1st Thread finishing...")
    
    
def func2():
    NS_APP.print(threading.main_thread(), 'Main Thread object: ')

    threading.current_thread().name = "February"
    NS_APP.print(threading.current_thread(), 'Thread Object: ')
    NS_APP.print(threading.get_ident(), 'Thread Ident: ')
    NS_APP.print(threading.get_native_id(), 'Thread Native Id: ')
    NS_APP.print(threading.current_thread().name, 'Thread Name: ')
    time.sleep(1)
    
    print("2nd Thread finishing...")


##############################
#### main code
##############################
t1 = threading.Thread(target = func1)
t2 = threading.Thread(target = func2)

NS_APP.print(threading.active_count(), '>>>>>> Thread Count: ')

NS_APP.print(threading.active_count(), '> Starting t1 ...')
t1.start()
NS_APP.print(threading.active_count(), '>>>>>> Thread Count: ')

NS_APP.print(threading.active_count(), '> Starting t2 ...')
t2.start()
NS_APP.print(threading.active_count(), '>>>>>> Thread Count: ')

