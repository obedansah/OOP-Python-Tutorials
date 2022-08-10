#Inheritance_Constructor

class Base:
    def __init__(self,r_no,name):
        print("Super Class Constructor")
        self.r_no = r_no
        self.name = name
        def dis(self):
            print(self.r_no , self.name)
            
        
class Derived(Base):
    def __init__(self, r_no, name,age):
        super().__init__(r_no, name)
        self.age = age   
        print("Subclass Constructor")
    def display(self):
        print(self.age)
        print(self.r_no , self.name , self.age)
        
        
D = Derived(23, "Smart" , 30)
D.display()
        