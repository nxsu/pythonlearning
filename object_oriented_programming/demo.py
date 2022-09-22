class students:
    
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def setdata(self):
        print('Accepting data')
        self.name = input("enter name: ")
        self.contact = input("enter contact: ")
    
    def getdata(self):
        print('The name is: '+ self.name + 'This is the contact: ' + self.contact) 

class sciencestudent(students):
    
    def __init__(self, age):
        self.age = age
    
    def science(self):
        print("i am a science student")

Rob = sciencestudent(20)
Rob.science()
Rob.setdata()
Rob.getdata()