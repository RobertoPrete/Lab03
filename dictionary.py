class Dictionary:
    def __init__(self, lingua):
        # self.parole = self.loadDictionary(f"resources/{lingua}.txt")
        self.parole = []
        self.lingua = lingua

    def loadDictionary(self, path):
        file_dizionario = open(path, "r")
        for line in file_dizionario:
            self.parole.append(line.split())
        file_dizionario.close()
        # return self.parole

    def printAll(self):
        for parola in self.parole:
            print(parola)

    def __contains__(self, item):
        if item in self.lingua:
            return True
        else:
            return False
    # @property
    # def parole(self):
    #    return self.parole
