from inspect import _void


class Student:
    def __init__(self,r_no , name):
        self.r_no = r_no
        self.name = name
    def display(self):
     print("Roll number is :" ,self.r_no)
     print("name is :" , self.name)
    
S1 = Student(10 , "Smart")
print("S1 Object info")
S1.display()
S2 = Student(12,"Obed")
print("S2 Object Info")
S2.display()
S3 = Student(20 , "Kwame")
S3.display()
