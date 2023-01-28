class dad:
    def __init__(self,flat,car,Fd):
        self.flat=flat
        self.car=car
        self.__FD=Fd
    def __shares(self):
        print("shares")
class son(dad):
    pass
obj=son("3bhk","audi",1000000)
print(obj.flat)
print(obj.__FD)
obj.__shares()