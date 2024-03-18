from threading import Thread, Lock
import time
import logging
from random import randrange
from sys import argv

mutex = Lock()
sharedBuffer = [] 
produttoriRunning = 0

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
    global produttoriRunning

    produttoriRunning += 1

    logging.info("{} sta partendo ...".format(nome))
    #logging.info("%s sta partendo ...", nome)

    with open(nomefile, 'r') as f:
        row = f.readline()
        while row:
            safeWrite(row[:-1])
            logging.info("{} ha letto dalla memoria condivisa la riga [{}]". format(nome, row[:-1])) 
            time.sleep(randrange(2))
            row = f.readline()

    produttoriRunning -= 1
    logging.info("{} sta terminando ...".format(nome))


def thread_consumatore(nome):
    global produttoriRunning
    global sharedBuffer

    logging.info("{} sta partendo ...".format(nome))

    while produttoriRunning > 0 or len(sharedBuffer) > 0:
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
    
    produttore1 = Thread(target=thread_produttore,  args=('Produttore1', argv[1],))
    produttore2 = Thread(target=thread_produttore,  args=('Produttore2', argv[2],))
    consumatore1 = Thread(target=thread_consumatore, args=('Consumatore1',))
    
    consumatore2 = Thread(target=thread_consumatore, args=('Consumatore2',))

    logging.info("Main       :  before running threads")

    produttore1.start()
    produttore2.start()
    time.sleep(0.1)
    consumatore1.start()
    consumatore2.start()
    
    logging.info("Main       :  wait for the threads to finish")

    produttore1.join()
    produttore2.join()
    consumatore1.join()
    consumatore2.join()

    logging.info("Main       :  all done")
