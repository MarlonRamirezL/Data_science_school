class Person:
    
    def __init__(self,name, age):
        self.name= name
        self.age= age

    def greet(self, other_person):
        return f'Hello {other_person.name}, My name is {self.name}'

    
    marlon= Person('Marlon',22)
    luisa= Person('Luisa', 24)

    marlon.greet(Luisa)
