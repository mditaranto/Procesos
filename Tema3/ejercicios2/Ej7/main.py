from queue import Queue
from threading import Condition
from consumidor import consumidor

from productor import Productor

if __name__ == "__main__":
    cola = Queue(1)
    cond = Condition()

    prod = Productor("Productor")
    cons = consumidor("Consumidor")
    prod.start()
    cons.start()
    