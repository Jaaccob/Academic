def xor(jeden, dwa):
    for i in range(len(jeden)):
        if int(jeden[i]) == 1 and dwa[i] == 1:
            jeden[i] = 0
        elif int(jeden[i]) == 1 and dwa[i] == 0:
            jeden[i] = 1
        elif int(jeden[i]) == 0 and dwa[i] == 1:
            jeden[i] = 1
        elif int(jeden[i]) == 0 and dwa[i] == 0:
            jeden[i] = 0
    return jeden


def szyfruj(plik_zrodlowy, plik_szyfrowany, maska):
    with open(f'{plik_zrodlowy}', 'rb') as file1, open(f'{plik_szyfrowany}', 'a') as file2:
        try:
            date = file1.read(1)
            while date:
                if date.decode() == '\n':
                    file2.write(date.decode())
                elif date.decode() == '\r':
                    pass
                else:
                    binary_byte = bin(int(date.hex(), base=16))[2:].zfill(8)
                    k = []
                    for bit in binary_byte:
                        k.append(bit)
                    tymcz = xor(k, [0, 0, 1, 1, 0, 1, 1, 1])
                    tymcz1 = 0
                    for i in range(len(tymcz)):
                        tymcz1 += int(tymcz[i]) * 2 ** (7 - i)
                    tymcz1 = chr(tymcz1)
                    file2.write(str(tymcz1))
                date = file1.read(1)
        finally:
            file1.close()
            file2.close()


if __name__ == "__main__":
    #    print("Podaj 3 arguemnty")
    #    plik_zrodlowy = input("Plik źródłowy:")
    #    plik_szyfrowany = input("Nazwa pliku do zaszyfrowania: ")
    #    maska = input("Maske w bitach: ")
    #    a_byte_array = bytearray(maska, "utf8")
    #    byte_list = []
    #    for byte in a_byte_array:
    #        binary_representation = bin(byte)
    #    byte_list.append(binary_representation)
    #    print(f'Zródło : {plik_zrodlowy}, szyfr: {plik_szyfrowany}, byte_list: {byte_list}')
    #    szyfruj(plik_zrodlowy, plik_szyfrowany, byte_list)
    szyfruj("Plik", "Plik_szyfrowany.txt", "00000011")
