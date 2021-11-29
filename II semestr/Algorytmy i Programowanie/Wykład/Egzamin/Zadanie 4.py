import Zadanie2


class HashTable:
    """
    Klasa HashTable odpowiedzialna jest za hashowanie tablic


    Attribute
    ---------
    cout: int
        Ilość list w tablicy hashującej

    Methods
    ------
    insert():
        Funkcja odpowiedzialna za dodoawanie nowych wartości do listy w tablicy

    hash_element():
        Funkcja odpowiedzialna za wyliczenie w której liście powinien znaleźć się element
    """
    def __init__(self, count):
        self.hash_table = []
        for i in range(count):
            self.hash_table.append([])

    def __str__(self):
        return str(self.hash_table)

    def insert(self, item):
        value = 0
        for i in range(5):
            if item[i] == "F":
                value += 1
            elif item[i] == "I":
                value += 0
            else:
                value += int(item[i])
        self.hash_table[self.hash_element(value)].append(item)

    def hash_element(self, element):
        return element % len(self.hash_table)


hashtable = HashTable(10)
bank = Zadanie2.Bank("f")
tablef = []
tablei = []
for i in range(5):
    tablef.append(bank.drukuj_numer())
    hashtable.insert(tablef[i])
bank = Zadanie2.Bank("i")
for i in range(5):
    tablei.append(bank.drukuj_numer())
    hashtable.insert(tablei[i])
print(hashtable)
