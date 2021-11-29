import FIFO
import random

Fifo = FIFO.FIFO

fifo = Fifo()
for x in range(random.randrange(1, 7)):
    y = random.randrange(0, 100)
    print("{} liczba to {}".format(x, y))
    fifo.addFirst(y)
for x in range(random.randrange(1, 7)):
    y = random.randrange(0, 50)
    print("{} liczba to {}".format(x, y))
    fifo.addLast(y)
fifo.printFIFO()
