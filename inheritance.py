class Parent():
    def __init__(self,eyecolor,money):
        print "Parent constructor is called !"
        self.eye = eyecolor
        self.mony = money

class Child(Parent):
    def __init__(self,eyecolor,money,toys):
        print "Child constructor is called ! "
        Parent.__init__(self,eyecolor,money)
        self.num_of_toys = toys


papa = Parent("blue",50)
print papa.mony
baccha = Child("red",100,12)
print baccha.num_of_toys
print baccha.eye
