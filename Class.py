class Student:
    r_no = 10
    name = "Smart"
    def display(self): #Function Definition
        r_no = 100 #local Variable
        print(r_no)
        print("Rol; no is:" , self.r_no) 
        print("Name is:" ,self.name)
S1 = Student() #Object 
S1.display() #Function Call 
S2= Student()
S2.r_no = 20
S2.name  ="Obed"
S2.display()