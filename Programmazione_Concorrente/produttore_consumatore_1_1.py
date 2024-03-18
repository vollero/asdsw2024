from threading import Thread, Lock
import time
import logging
from random import randrange
from sys import argv

mutex = Lock()
sharedBuffer = [] 
produttoreRunning = True

def safeWrite(row):
    global sharedBuffer
    global mutex

    mutex.acquire()
    sharedBuffer.append(row)
    mutex.release()

def safeRead():
    global sharedBuffer
    global mutex

    mutex.acquire()
    row = sharedBuffer[0]
    sharedBuffer.remove(row)
    mutex.release()

    return row

def thread_produttore(nome, nomefile):
    global produttoreRunning

    logging.info("{} sta partendo ...".format(nome))
    #logging.info("%s sta partendo ...", nome)

    with open(nomefile, 'r') as f:
        row = f.readline()
        while row:
            safeWrite(row[:-1])
            logging.info("{} ha letto dalla memoria condivisa la riga [{}]". format(nome, row[:-1])) 
            time.sleep(randrange(2))
            row = f.readline()

    produttoreRunning = False
    logging.info("{} sta terminando ...".format(nome))


def thread_consumatore(nome):
    global produttoreRunning
    global sharedBuffer

    logging.info("{} sta partendo ...".format(nome))

    while produttoreRunning or len(sharedBuffer) > 0:
        if len(sharedBuffer) > 0:
            row = safeRead()
            logging.info("{} ha letto dalla memoria condivisa la riga [{}]". format(nome, row))
        else:
            time.sleep(randrange(2,5))

    logging.info("{} sta terminando ...".format(nome))


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main       :  before creating threads")
    
    
    produttore  = Thread(target=thread_produttore,  args=('Produttore', argv[1],))
    consumatore = Thread(target=thread_consumatore, args=('Consumatore',))
    
    logging.info("Main       :  before running threads")

    produttore.start()
    consumatore.start()
    
    logging.info("Main       :  wait for the threads to finish")

    produttore.join()
    consumatore.join()

    logging.info("Main       :  all done")
