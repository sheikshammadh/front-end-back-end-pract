'''
wrapping of var. and meth. into single unit.

public
private__
protected_
'''
# ==============================================================
'''
class show():
    __a=100# private
    _b=10 # protected
    print(__a) #100
    print(_b) #10
    '''
#  ============================
class A1():
    def __init__(self,a,b):
        self.__a=a#private class
        self._b=b#protected class
class B1(A1):
    def output(self):
        print(self.__a)
d=B1(5,6)
d.output()#6(5 stored in "a" and 6 stored in "b") it gives output bcz it is private.
d.output()#'B1' object has no attribute '_B1__a'.   it doesnr give bcz it is protected.


class emp:
    def set_ename(self,name):
        self.set_ename=name
    def get_ename(self):
        return self.set_ename
e1=emp()
e1.set_ename("shyam")
print(e1.get_ename())

e2=emp()
e2.set_ename("asdfghjkl")
print(e2.get_ename())
