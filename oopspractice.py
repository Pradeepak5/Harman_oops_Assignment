#inheritance
class Phone:
    def __init__(self,Brand,Model,Phonecolor,ReleaseYear,Price):
        self.brand=input("Mobile Brand :")
        self.model=input("Mobile Model :")
        self.phonecolor=input("PhoneColor :")
        self.releaseyear=int(input("ReleseYear :"))
        self.price=int(input("Price :"))

    def PrintPhone(self):
        print("Brand :",self.brand)
        print("Model :",self.model)
        print("Color :",self.phonecolor)
        print("Release Year :",self.releaseyear)
        print("Price :",self.price)

class Discount(Phone):
    def __init__(self,Brand,Model,Phonecolor,ReleaseYear,Price,Discount):
        self.discount=input("Discount :")
        Phone.__init__(self,Brand,Model,Phonecolor,ReleaseYear,Price)

    def PrintDiscount(self):
        print("Discount :",self.discount,"%")

x=Discount("Brand","Model","Phonecolor","ReleaseYear","Price","Discount")
x.PrintPhone()
x.PrintDiscount()

#Overriding

class likhi:
    def Manager(self):
        print("Likhitha is content Manager")

class Pradeep(likhi):
    def Manager(self):
        super().Manager()
        print("Pradeep is also content manager")

a=Pradeep()
a.Manager()

#encapsulation
class FoodPrice:
    def __init__(self):
        self.__price=100

    def viewFoodPrice(self):
        print(self.__price)

    def ChangePrice(self,price):
        self.__price=price

x=FoodPrice()
x.viewFoodPrice()
x.ChangePrice("120")
x.viewFoodPrice()

