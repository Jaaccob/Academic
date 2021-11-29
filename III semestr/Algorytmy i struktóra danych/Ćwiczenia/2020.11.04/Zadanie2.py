import Fifo

kolejka = Fifo.Kolejka_Fifo


class Stack():
    def __init__(self, n):
        queueOne = kolejka(n)
        queueTwo = kolejka(n)
