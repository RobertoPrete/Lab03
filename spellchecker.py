import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.parole_errate = []
        self.numero_parole_errate = 0
        self.tempo_controllo_ortografico = 0

    def handleSentence(self, txtIn, language, istanza_md):
        txtIn = replaceChars(txtIn)
        lista_parole = txtIn.split(" ")
        self.parole_errate.extend(istanza_md.searchWord(lista_parole, language))
        self.numero_parole_errate = len(self.parole_errate)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def printParoleErrate(self):
        for parola in self.parole_errate:
            print(parola)


def replaceChars(text):
    chars = "\\'*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text