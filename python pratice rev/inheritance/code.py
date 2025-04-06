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
# one parent class and one child class


class parnent():
    def display(self):
        print("parent class")
class child(parnent):
    def show(self):
        print("child class")
a=child()
a.display()#parent class
a.show()#child class


class shyam():
    def me(self):
        print("iam the father of sana")
class sana(shyam):
    def her(self):
        print("iam the child")
a=sana()#   defining the a with child class
a.me()# ian=m the father of sana
a.her()# iam the child

# ======================================================================

# multi level inheritance.
# having more parent classes more than one.

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

# ==============================================================
# multiple inheritance.
# having two parent class and one child class.

class father():
    def parent1(self):
        print("iam the father")
class mother():
    def parent2(self):
        print("iam the mother")
class child(father,mother):# accessing the both parent classes
    def childself(self):
        print("iam the child")
a=child()#defining a as child()
a.parent1()#iam the father.
a.parent2()# iam the mother.
a.childself()# iam the child.

# ================================================================
#hierarchical inheritance

class father():#we can use any class name
    def parent(self):# we can use any method name
        print("iam the father")#father class method 
class child1(father):
    def child_1(self):
        print("iam the child 1")#child class method
class child2(father):
    def child_2(self):
        print("iam the child 2")
class child3(father):
    def child_3(self):
        print("iam the child 3")
class child4(father):
    def child_4(self):
        print("iam the child 4")
#invocations
a1=child1()#child 1 class object creation
a2=child2()#child 2 class object creation
a3=child3()#child 3 class object creation
a4=child4()#child 4 class object creation
a.parent()#father class method
a1.child_1()#child class method
a2.child_2()#child 2
a3.child_3()#child 3
a4.child_4()#child 4
# ================================================================

 