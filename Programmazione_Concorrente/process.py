# See "Distributed Systems" - Van Steen, Tanenbaum - Ed. 4 (p. 117)

from multiprocessing import Process
from time import *
from random import *

global value

def sleeper(name):
    global value
    t = gmtime()
    s = randint(4,20)
    value = s
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' is going to sleep for ' + str(s) + ' seconds ' 
    #+ str(value) 
    print(txt)
    sleep(s)
    t = gmtime()
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' has woken up ' + str(value)
    print(txt)

if __name__ == '__main__':
    process_list = list()
    global value
    for i in range(10):
        p = Process(target=sleeper, args=('mike_{}'.format(i),))
        process_list.append(p)

    print('tutti i processi sono pronti')

    for i, p in enumerate(process_list): 
        #value = i
        p.start()
        sleep(0.1)

    print('tutti avviati')

    for p in process_list: p.join()

    print('tutti terminati!')
