class Company:
    def __init__(self,name,revenue):
        self._name=name   
        self._revenue=revenue

    def show_company(self):
        print(f"Company:{self._name}, Revenue; Rs{self._revenue}")

class Branch(Company):
    def show_branch(self):
        print(f"Branch of{self._name}, Revenue: Rs{self._revenue}")

comp=Branch("TechCorp",1000000)

print(comp._name)
print(comp._revenue)

comp.show_company()
comp.show_branch()