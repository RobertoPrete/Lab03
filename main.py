import spellchecker

sc = spellchecker.SpellChecker()

import multiDictionary

md = multiDictionary.MultiDictionary()

import dictionary
ita_dic = dictionary.Dictionary("Italian")
eng_dic = dictionary.Dictionary("English")
spa_dic = dictionary.Dictionary("Spanish")

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        ita_dic.loadDictionary("resources/Italian.txt")
        md.aggiungiDizionario("Italian", ita_dic)
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn, "Italian", md)
        print(f"Le parole errate sono {sc.numero_parole_errate}:")
        sc.printParoleErrate()
        continue

    if int(txtIn) == 2:
        eng_dic.loadDictionary("resources/English.txt")
        md.aggiungiDizionario("English", eng_dic)
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn, "English", md)
        print(f"The wrong words are {sc.numero_parole_errate}:")
        sc.printParoleErrate()
        continue

    if int(txtIn) == 3:
        spa_dic.loadDictionary("resources/Spanish.txt")
        md.aggiungiDizionario("Spanish", spa_dic)
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn, "Spanish", md)
        print(f"Las palabras equivocadas son {sc.numero_parole_errate}:")
        sc.printParoleErrate()
        continue

    if int(txtIn) == 4:
        break

    print()
