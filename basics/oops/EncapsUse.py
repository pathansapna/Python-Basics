class EncapsUse:

#Creating hidden object to achieve encapsulation
    def __init__(self):
        self.__max_price = 2500

    def sell(self):
        return f'selling price: {self.__max_price}'

    def set_max_price(self, price):
        if price > self.__max_price:
            self.__max_price = price


#Object
encaps_obj = EncapsUse()
print(encaps_obj.sell())

#Trying to modifying price directly
encaps_obj.__max_price = 3500
print(encaps_obj.sell())

#Modifying price using setter function
encaps_obj.set_max_price(4500)
print(encaps_obj.sell())