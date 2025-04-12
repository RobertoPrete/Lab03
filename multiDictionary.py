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
            if self.multi_dizionario.get(language).parole.__contains__(rich_word):
                # rich_word.corretta(True)     non so perchè se eseguo questa riga non esegue il setter ma il getter
                rich_word.corretta = True
                parole_errate.append(rich_word.parola)
                break
            else:
                # rich_word.corretta(False)
                rich_word.corretta = False
        return parole_errate

    def aggiungiDizionario(self, language, dizionario):
        self.multi_dizionario.update({language: dizionario})
        # self.multi_dizionario.update({language: dizionario.parole})


    def getDizionario(self, language):
        return self.multi_dizionario[language]
