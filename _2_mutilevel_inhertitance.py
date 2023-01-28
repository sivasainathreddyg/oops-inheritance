# class grandpa:
#     def field(self):
#         print("Field")

# class dad(grandpa):
#     def flat(self):
#         print("Flat")
#     def car(self):
#         print("Car")

# class son(dad):
#     def bike(self):
#         print("Bike")
#     def mobile(self):
#         print("Mobile")

# obj = son()
# obj.bike()
# obj.mobile()
# obj.flat()
# obj.car()
# obj.field()



class area_of_Circle:
    def circle_area(self,radius):
        return (3.14*radius*radius)
    def arae_of_square(self,side):
        return (side*side)
    def area_of_triangle(self,length,breadth):
        return (0.5*length*breadth)
    def area_of_rectangle(self,length,breadth):
        return (length*breadth)
class area(area_of_Circle):
    pass
obj=area()
print(obj.circle_area(10))
print(obj.area_of_rectangle(10,5))