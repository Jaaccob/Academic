import math

from Osoba import Osoba


class HashTable:
    def __init__(self, count):
        self.count = count
        self.hash_table = []
        for i in range(self.count):
            self.hash_table.append([])

    def __str__(self):
        return str(self.hash_table)

    def insert(self, item):
        self.hash_table[self.hash_element_modulo(item.pesel)].append(item)

    def hash_element_modulo(self, element):
        return element % self.count

    def hash_element_gold_number(self, element):
        global A
        #m*(k*A)%1
        k = len(element.imie) + len(element.nazwisko) + element.pesel
        v = self.count * ((k * A) % 1)
        return v

    def remove(self, item):
        new_bucket = []
        print(self.hash_element_modulo(item.pesel))
        for j in self.hash_table[self.hash_element_modulo(item.pesel)]:
            print(j)
            if j != item:
                new_bucket.append(j)
        self.hash_table[self.hash_element_modulo(item.pesel)] = new_bucket

    def search(self, item):
        for i in self.hash_table[self.hash_element_modulo(item.pesel)]:
            if i == item:
                return True
        return False


person_one = Osoba("Jakub", "Kozubek", 121932109)
person_two = Osoba("Wojciech", "Witos", 121973192)
person_tree = Osoba("Bartosz", "Baranowicz", 312921030)
person_four = Osoba("Patrycja", "Błachut", 192910305)

ht = HashTable(5)
ht.insert(person_one)
ht.insert(person_two)
ht.insert(person_tree)
ht.insert(person_four)
print(ht)
ht.remove(person_tree)
print(ht)
print(ht.search(person_two))
