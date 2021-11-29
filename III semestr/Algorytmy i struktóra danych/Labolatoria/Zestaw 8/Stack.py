class Stack:
    """Implementacja stosu za pomoca listy Pythona, czyli klasycznej tablicy"""

    def __init__(self):
        """inicjalizacja"""
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        """wlozenie elementu na (szczyt) stos"""
        self.items.append(item)

    def pop(self):
        """sciagniecie elementu ze (szczytu) stosu"""
        return self.items.pop()

    def top(self):
        """zwrocenie elementu ze (szczytu) stosu"""
        return self.items[len(self.items) - 1]

    def size(self):
        """zwrocenie rozmiaru stosu"""
        return len(self.items)


