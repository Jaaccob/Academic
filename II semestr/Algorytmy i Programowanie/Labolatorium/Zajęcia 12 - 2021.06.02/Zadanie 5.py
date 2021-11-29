class Word:
    def __init__(self, string):
        self.string = string
        self.length = len(self.string)

    def reverse(self):
        reverse_string = ""
        for i in range(len(self.string), 0, -1):
            reverse_string += self.string[i - 1]
        return reverse_string

    def shorted(self):
        return self.string[:3]

    def __str__(self):
        return f"Słowo jest obiektem klasy Word o długości {self.length}"

    def __add__(self, other):
        new_string = self.string + other.string
        return Word(new_string)

    def __repr__(self):
        return self.string

    def __call__(self, *args, **kwargs):
        print(self.string)


napis1 = Word("napis")
print(napis1.reverse())
print(napis1.shorted())
napis2 = Word("sipan")
napis3 = napis1 + napis2
print(napis3.string)
napis3()
