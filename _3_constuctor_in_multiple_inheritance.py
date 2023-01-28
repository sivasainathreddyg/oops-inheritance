class mom:
    def __init__(self,name):
        self.name=name
        print("mom constructor")
    def property(self):
        print("jewwllary")

class dad:
    def __init__(self,address):
        self.address=address
        print("dad constructor")
    def property(self):
        print("Flat")

class son(dad,mom):
    def __init__(self, age):
        mom.__init__(self,"abc")
        dad.__init__(self,"xyz")
        self.age=age
    def property(self):
        mom.property(self)
        dad.property(self)
        print("mobile")
obj=son(18)
obj.property()