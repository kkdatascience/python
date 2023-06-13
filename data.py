#class creation of child class
class add(calculation):
    def display_sum(self):
        res=self.a+self.b
print ('sum is two is',res)

#object creation with child class
add1=add(10,20)
add1.display()
add1.display_sum()

#parent class object creation
cal=calculation(10,19)
cal.display().