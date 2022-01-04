class Pessoa:
    """ Essa é a classe Pessoa """
    _CPF=''
    _nome=''
    _datanasc=''
    _endereco=''
    _sexo=''

    def __init__(self, cpf='', nome='', datanasc='', endereco='', sexo=''):
        self._nome=nome
        self._CPF=cpf
        self._datanasc=datanasc
        self._endereco=endereco
        self._sexo=sexo
    
    def get_CPF(self):
        return self._CPF
      
    def set_CPF(self, cpf):
        self._CPF = cpf

    def get_nome(self):
        return self._nome
      
    def set_nome(self, nome):
        self._nome = nome
    
    def get_datanasc(self):
        return self._datanasc
      
    def set_datanasc(self, datanasc):
        self._datanasc = datanasc

    def get_endereco(self):
        return self._endereco
      
    def set_endereco(self, endereco):
        self._endereco = endereco
    
    def get_sexo(self):
        return self._sexo
      
    def set_sexo(self, sexo):
        self._sexo = sexo

