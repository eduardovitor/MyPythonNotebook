
class Disciplina:
    _nome=''
    _cod=''
    def __init__(self, nome, cod):
        self._nome=nome
        self._cod=cod
    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome=nome
    def getCod(self):
        return self._cod
    def setCod(self, cod):
        self._cod=cod