# class Dad:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_dad_info(self):
#         return f"name:{self.name}\nage :{self.age}"
# class Son(Dad):
#     def __init__(self,name,age,occupation):
#         super().__init__(name,age)
#         self.occupation=occupation
#     def display_son_info(self):
#         return f"sons occupation:{self.occupation}"

# son=Son("siva",21,"develpoer")
# print(son.display_dad_info())
# print(son.display_son_info())

# #self--represents current class object
# #super--- represents immediate parent class object 


# class dad:
#     def property(self):
#         print("Flat and Car")

# class son(dad):
#     def property(self):
#         print("MObile and bike")
# obj=son()
# obj.property()


# class dad:
#     def property(self):
#         print("Flat and Car")

# class son(dad):
#     def property(self):
#         super().property()
#         print("MObile and bike")
# obj=son()
# obj.property()


class Collage:
    def __init__(self,collage_name,collage_address):
        self.collage_name=collage_name
        self.collage_address=collage_address
    def dispaly(self):
        print(f"collage_name:{self.collage_name}\ncollage_address:{self.collage_address}")
class Student(Collage):
    def __init__(self,student_name,student_address,collage_name,collage_address):
        super().__init__(collage_name,collage_address) 
        self.student_name=student_name
        self.student_address=student_address
    def dispaly(self):
        super().dispaly()
        print(f"student_name:{self.student_name} \nstudent_address:{self.student_address}")
student=Student('siva','andhrapradesh','Edyoda','banglore')
student.dispaly()


