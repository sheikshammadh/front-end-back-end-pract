'''
parnent class or base class
child class or derived class
''' 
'''
single inhertance
multi level inheritance
multiple inheritance
hierarchical inhertance
'''
# ==================================================================
# sinlge inheritance

'''
class parnent():
    def display(self):
        print("parent class")
class child(parnent):
    def show(self):
        print("child class")
a=child()
a.display()#parent class
a.show()#child class
'''
'''
class shyam():
    def me(self):
        print("iam the father of sana")
class sana(shyam):
    def her(self):
        print("iam the child")
a=sana()#   defining the a with child class
a.me()# ian=m the father of sana
a.her()# iam the child
'''
# ======================================================================
'''
# multi level inheritance.

class grandfather():
    def third(self):
        print("iam the grandfather")
class father(grandfather):
    def second(self):
        print("iam the father of child")
class child(father):
    def first(self):
        print("iam the child")
a=child()
a.third()#grandfather
a.second()# father of child
a.first()#child
'''
# ==============================================================
