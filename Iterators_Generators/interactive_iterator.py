
class InteractiveIterator():
    def __init__(self, initial_value):
        self.__initial_value = initial_value
        self.__step = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.__initial_value += self.__step
        return self.__initial_value
    def send(self,new_step):
        return self.__initial_value + new_step

int_iter = InteractiveIterator(10)
print(next(int_iter))
print(next(int_iter))
print(int_iter.send(5))
print(next(int_iter))

