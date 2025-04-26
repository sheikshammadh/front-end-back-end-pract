
# #adding the different forms in one unit.
# def add(shyam,nandu):
#     print(shyam+nandu)
# add(5,3)#8 (concat)
# add(124,145)#269 (concat)
# add("shyam","nandu")#shyamnandu (concat)
# add(234.441,214314.134325)#214548.57532499998 (concat)
# add([124,134],[124,14314])#[124, 134, 124, 14314] (concat)

# ====================================================================================================================
class emp():
    def calc_tax(self):
        print("empl clc tax")

class pe(emp):
    def calc_tax(self):
        print("pe clc tax")
class ce(emp):
    def calc_tax(self):
        print("ce clc tax")
def execute(obj):
    obj.calc_tax()
execute(emp())
execute(pe())
execute(ce())
