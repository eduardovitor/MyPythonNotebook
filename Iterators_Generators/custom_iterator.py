class Contador:
    def __init__(self,inicio,fim):
        self.__inicio = inicio
        self.__fim = fim
    def __iter__(self):
        return self
    def __next__(self):
        if self.__inicio <= self.__fim:
            r = self.__inicio
            self.__inicio += 1
            return r
        else:
            raise StopIteration

        

c = Contador(1,10)
print(list(c))