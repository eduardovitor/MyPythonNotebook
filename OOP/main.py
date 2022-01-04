from Disciplina import Disciplina
from Pessoa import Pessoa
from Aluno import Aluno
from Professor import Professor
disciplinas=[]
disciplinas.append(Disciplina('Matemática','123'))
disciplinas.append(Disciplina('Português','456'))
disciplinas.append(Disciplina('Quimíca','789'))
num_turmas=[]
num_turmas.append('888')
num_turmas.append('121')
pessoa=Pessoa('123', 'Júnior','23/02/2007', 'Rua João', 'M')
aluno=Aluno('222',disciplinas)
professor=Professor('Bacharelado em Sistemas da Informação',disciplinas, num_turmas)
print('Dados da pessoa: \n')
print('Nome: {}'.format(pessoa.get_nome()))
print('CPF: {}'.format(pessoa.get_CPF()))
print('Data de nascimento: {}'.format(pessoa.get_datanasc()))
print('Endereco: {}'.format(pessoa.get_endereco()))
print('Sexo: {}'.format(pessoa.get_sexo()))