import dictionary as d
import richWord as rw


class MultiDictionary:
    def __init__(self):
       self.multi_dizionario = {}

    def printDic(self, language):
        d.Dictionary(language).printAll()

    def searchWord(self, words, language):
        parole_errate = []
        for word in words:
            rich_word = rw.RichWord(word)
            parola = rich_word.parola.lower().strip()
            if self.multi_dizionario.get(language).parole.__contains__(parola):
                rich_word.corretta = True
            else:
                rich_word.corretta = False
                parole_errate.append(rich_word.parola)
        return parole_errate

    def aggiungiDizionario(self, language, dizionario):
        self.multi_dizionario.update({language: dizionario})

    def getDizionario(self, language):
        return self.multi_dizionario[language]
