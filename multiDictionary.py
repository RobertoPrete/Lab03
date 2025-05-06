import dictionary as d
import richWord as rw


class MultiDictionary:
    def __init__(self):
       # self.multi_dizionario = {"Italian": d.Dictionary("Italian"),
       #                         "English": d.Dictionary("English"),
       #                        "Spanish": d.Dictionary("Spanish")}
       self.multi_dizionario = {}

    def printDic(self, language):
        # dizionario = self.multi_dizionario.get(language)
        # dizionario.printAll()
        d.Dictionary(language).printAll()

    def searchWord(self, words, language):
        parole_errate = []
        for word in words:
            rich_word = rw.RichWord(word)
            parola = rich_word.parola.lower().strip()
            if self.multi_dizionario.get(language).parole.__contains__(parola):
                # rich_word.corretta(True)     non so perchè se eseguo questa riga non esegue il setter ma il getter
                rich_word.corretta = True
            else:
                # rich_word.corretta(False)
                rich_word.corretta = False
                parole_errate.append(rich_word.parola)
        return parole_errate

    def aggiungiDizionario(self, language, dizionario):
        self.multi_dizionario.update({language: dizionario})
        # self.multi_dizionario.update({language: dizionario.parole})


    def getDizionario(self, language):
        return self.multi_dizionario[language]
