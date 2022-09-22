class Human():
    def __init__(self, id, name):
        self.name = name
        self.id = id
        print(id , name)

    def uniform(self):
        print("Dress Regular!")

class Employee(Human):
    def __init__(self, id, name):
        super().__init__(id, name)
    
    def uniform(self):
        print("Dress Casual!")
        
    def set_name(self, name):
        self.name = name
        
class Manager(Employee): 
    def __init__(self, id, name): 
        super().__init__(id, name)
        
    def uniform(self):
        print("Dress Suits!") 
       
class Project(): 
    def __init__(self, id, name):
        self.id = id
        self.name = name

file = open('readme.txt', 'r')
read = file.readlines()
for x in read:
    y = x.strip().split(" ")
    g = f"{y[0]}({y[1]},{y[2]})"
    print(g)
    compiled = compile(g, '', 'exec')
    exec(compiled)




