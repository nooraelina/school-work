class A:

    def __init__(self, name, id : str):
        self.name = name
        self.id = id 

    @property
    def id (self): return self.__id

    @id.setter
    def id(self, id : str):
        if id :  self.__id = id
        else :  self.__id = 'unknown'

    def method(self):
        return f"Type {type(self)}'s method object name {self.name} and id {self.__id}"

class B:

    def __init__(self, name, id, obs : A):
        if type(obs) is A: self.a = obs
        else : self.a = A('unknown', 0)
        self.c = B.C(name + ' (c)', id * (-1))
        self.name = name
        self.__id = id

    def method(self):
        return f"Type {type(self)}'s method, object name {self.name} and id {self.__id}\n" \
                f"\tCalling type {type(self.c)}'s method, object name {self.a.name} and id {self.a.id}\n" \
                f"\tAnd calling also type {type(self.c)}'s method, object name {self.c.name} and id {self.c.id}\n"   

    class C:

        def __init__(self, name, id):
            self.name = name
            self.id = id

        @property
        def id (self): return self.__id

        @id.setter
        def id(self, id : int):
            if type(id) is int : self.__id = id
            else: self.__id = -100

        def method(self):
            return f"Type {type(self)}'s method, object name {self.name} and id {self.__id}"

a = A('moi', 'jee')
b = B('jee')
print(a.method())