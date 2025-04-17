# class empl:
#     org_name='TCS'
#     def __init__(self,id,ename,salary):
#         self.id=id
#         self.ename=ename
#         self.salary=salary
    
        
# e1=empl(101,'rg',13425)
# e2=empl(102,'gg',136543)
# e3=empl(103,'dg',1347654)

# print(e1.__dict__)
# print(e2.__dict__)
# print(e3.__dict__)
# print(empl.__dict__)

# class empl():
    
#     def __init__(self):
#         self.a=10
#     def m1(self):
#         self.b=100
#     @classmethod
#     def m2(cls):
#         # cls.c=1000
#         pass
#     @staticmethod
#     def m3():
#         pass
        
# t1=empl()
# t1.e=20
# t1.m1()
# t1.m2()
# t1.m3()
# del t1.b

# t2=empl()
# t2.f=10000

# print(t1.__dict__)
# print(t2.__dict__)

# ================================================================================================================================================
#Static variable:
# inside a class -directly
# inside a constructor -by class name
# inside a ins.meth - by class name
# inside a method - by class& cls name
# inside a staticmethod- class name
# inside a class - using class name


# class empl():
#     a=11
#     def __init__(self):
#         empl.b=101
#     def m1(self):
#         empl.c=100
#     @classmethod
#     def m2(cls):
#         cls.d=1000
#         empl.e=102
#     @staticmethod
#     def m3():
#         empl.f=12
    
# t1=empl()
# t2=empl()
# # t1.e=20
# t1.m1()
# t1.m2()
# t1.m3()
# empl.g=40
# # del t1.b

# print(empl.__dict__)
# print(t1.__dict__)
# print(t2.__dict__)


# class parent:
#     def m1(self):
#         print("parent meth m1")
#     def m2(self):
#         print("parent meth m2")
# class child(parent):
#     def m3(self):
#         print("child meth m3")
        
# a1=child()
# a1.m1()#parent meth m1
# a1.m2()#parent meth m2
# a1.m3()#child meth m3


