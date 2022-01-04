from Pessoa import Pessoa

#herança em Python
class Professor(Pessoa):
    """ Essa é a classe Professor"""
    def __init__(self, formacao, disciplinas, num_turmas):
        super().__init__()
        self._formacao=formacao
        self._disciplinas=disciplinas
        self._num_turmas=num_turmas

    def get_Formacao(self):
        return self._formacao
      
    def set_Formacao(self, formacao):
        self._formacao = formacao

    def get_Disciplinas(self):
        return self._disciplinas
      
    def set_Disciplinas(self, disciplinas):
        self._disciplinas = disciplinas
    
    def get_NumTurmas(self):
        return self._num_turmas
      
    def set_NumTurmas(self, num_turmas):
        self._num_turmas = num_turmas
    
