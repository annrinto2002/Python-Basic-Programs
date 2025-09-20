class Company:
    def __init__(self,name,revenue):
        self._name=name    # Protected attribute
        self._revenue=revenue # Protected attribute

    def show_company(self):
        print(f"Company:{self._name}, Revenue; Rs{self._revenue}")

class Branch(Company):
    def show_branch(self):
        print(f"Branch of{self._name}, Revenue: Rs{self._revenue}")

#Creating an object
comp=Branch("TechCorp",1000000)

#Accessing protected attributes
print(comp._name) #Not recommended but allowed
print(comp._revenue) #Not recommended but allowed

#Calling methods
comp.show_company()
comp.show_branch()
