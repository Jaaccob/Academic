def gen_doc_google(slownik):
    args = ""
    attr = ""
    for i in slownik["Args"]:
        args += i + ":\n"
    for i in slownik["Attributes"]:
        attr += i + ": tu przechowujemy informacje o parametrze " + i + "\n"
    return f'{slownik["Summary"]}\n\n' \
           f'Args:\n' \
           f'{args}\n' \
           f'{attr}\n\n' \
           f'{slownik["Description"]}'


print(gen_doc_google({'Args': ['a', 'b'],
                      'Attributes': ['a', 'b'],
                      'Summary': "Obiekt Gruszka opisuje nam wlasnosci gruszek.",
                      'Description': "Opis tej funkcji"}))
