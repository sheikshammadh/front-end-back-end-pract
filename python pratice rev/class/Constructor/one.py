# class acc():
#     pass

#acc()

# class acc():
#     pass

# acc(1,2,3,4).

# class Acc():
#     def __init__(self):
#         print("constructor is a special method")
#     def dep_amt(self):
#         print("dep")
#     @classmethod
#     def update_amt(cls):
#         print("upd")
#     @staticmethod
#     def sum_num(a,b):
#         print("stc meth")
# Acc()
# Acc.dep_amt(10)
# Acc.update_amt()
# Acc.sum_num(1,2)



# class Acc():
#     def __init__(self,id,name,amount):
#         self.id=id
#         self.name=name
#         self.acc_bal=amount
#     def dep_amt(self,amount):
#         self.acc_bal=self.acc_bal+amount
#     # @classmethod
#     # def update_amt(cls):
#     #     pass

#     # @staticmethod
#     # def sum_num(a,b):
#     #     pass
# a1=Acc(101,"abc",45000)
# a1.dep_amt(100)
# print(a1.__dict__)#{'id': 101, 'name': 'abc', 'acc_bal': 45100}
# a2=Acc(102,"cde",65000)
# a2.dep_amt(200)
# print(a2.__dict__){'id': 102, 'name': 'cde', 'acc_bal': 65100}
# ========================================================================================================================================]
# class Acc():
#     def __init__(self,id,name,amount):
#         self.id=id
#         self.name=name
#         self.acc_bal=amount
#     def dep_amt(self,amount):
#         self.acc_bal=self.acc_bal+amount
#     def withdr_amt(self,amount):
#         self.acc_bal=self.acc_bal-amount
        
# a1=Acc(101,"abc",45000)
# a1.dep_amt(100)
# a1.withdr_amt(10)
# print(a1.__dict__)

# a2=Acc(102,"cde",65000)
# a2.dep_amt(200)
# a2.withdr_amt(10)#{'id': 101, 'name': 'abc', 'acc_bal': 45090}
# print(a2.__dict__)#{'id': 102, 'name': 'cde', 'acc_bal': 65190}


# class Acc():
#     a=10 # class variable
#     def __init__(self):
#         self.b=10 # instance variable are used when the variable values are varied.
#         self.c=20 # instance variable
#     def open_acc(self):
#         self.d=30
# a1=Acc()
# print(a1.__dict__)#{'b': 10, 'c': 20}
# print(Acc.__dict__)# adds some extra attributes internally
'''{'__module__': '__main__', 'a': 10, '__init__': <function Acc.__init__ at 0x0000022555C8D3A0>,
'open_acc': <function Acc.open_acc at 0x0000022555C8DF80>,
'__dict__': <attribute '__dict__' of 'Acc' objects>,
'__weakref__': <attribute '__weakref__' of 'Acc' objects>, '__doc__': None}
'''
# ============================================================================================================
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


class empl():
    a=11
    def __init__(self):
        empl.b=101
    def m1(self):
        empl.c=100
    @classmethod
    def m2(cls):
        cls.d=1000
        empl.e=102
    @staticmethod
    def m3():
        empl.f=12
    
t1=empl()
t2=empl()
# t1.e=20
t1.m1()
t1.m2()
t1.m3()
empl.g=40
# del t1.b

print(empl.__dict__)
print(t1.__dict__)
print(t2.__dict__)




