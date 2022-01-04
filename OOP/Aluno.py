from Pessoa import Pessoa

#herança em Python
class Aluno(Pessoa):
    """ Essa é a classe Aluno"""
    def __init__(self, num_matricula, disciplinas):
        super().__init__('','','','','')
        self._num_matricula=num_matricula
        self._disciplinas=disciplinas

    def get_NumMatricula(self):
        return self._num_matricula
      
    def set_NumMatricula(self, num_matricula):
        self._num_matricula = num_matricula

    def get_Disciplinas(self):
        return self._disciplinas
      
    def set_Disciplinas(self, disciplinas):
        self._disciplinas = disciplinas