#SINGLE INHERITANCE
'''class rbi():
    cash = 100000
    def available_cash(cls):
        print("available cash is:", cls.cash)
        print("available cash is:", rbi.cash)
class sbi(rbi):
    pass
class hdfc(rbi):
    cash = 50000
    def new_cash(cls):
        print("new cash is:", cls.cash+cls.cash)
        print("new cash is:", cls.cash+rbi.cash)
a = hdfc()
a.available_cash()
a.new_cash()'''

'''class rbi():
    cash = 100000
    def available_cash(cls):
        print("available cash is:", cls.cash)
        print("available cash is:", rbi.cash)
class sbi(rbi):
    cash = 25000
    def old_cash(cls):
        print("new cash is:", cls.cash)
        print("old cash is:", cls.cash+hdfc.cash)
class hdfc(sbi):
    cash = 50000
    def new_cash(cls):
        print("new cash is:", cls.cash+cls.cash)
        print("new cash is:", cls.cash+sbi.cash)
a = hdfc()
b = sbi()
a.available_cash()
a.new_cash()
b.old_cash()'''

#MULTIPLE INHERITANCE
'''class father():
    weight = 70
    def fweight(self):
        print("weight (in parent class):", self.weight)
class mother():
    height = 5.5
    def mheight(self):
        print("height (in parent class):", self.height)
class child(father,mother):
    dob = 'sep1 2004'
    def child_fun(self):
        print("weight (in child class):", self.weight)
        print("height (in child class):", self.height)
a = child()
a.child_fun()
a.fweight()
a.mheight()'''

#MULTILEVEL INHERITANCE
'''
class grand_parent():
    def acres(self):
        print("100 acres")
class parent(grand_parent):
    def house(self):
        print("1 duplex house")
class child(parent):
    def bike(self):
        print("1 car")
a = child()
a.bike()
a.house()
a.acres()
'''
