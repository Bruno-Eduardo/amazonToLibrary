from forex_python.converter import CurrencyRates

class Book:
    #args = (   unidade, seq, author, title, publisher, vol, year, edition, ISBN10, ISBN13, priority, quantity
    #           unitValue, totalValue, observation, internationalFlag, unitValueWithTAxes, totalValuewithTaxesBRL, dollarPrice):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
            #expecting  unidade, seq, author, title, publisher, vol, year, edition, ISBN10, ISBN13, priority, quantity,
            #           unitValue, observation
        self.totalValue = round(self.getTotalValue(),2)

    def getTotalValue(self):
        return self.unitValue*self.quantity

    def __str__(self):
        out = ""
        out += "This is a book. Attrs:"
        out += str(vars(self))
        return out

class nationalBook(Book):
    def __init__(self, **kwargs):
        self.internationalFlag = False
        super(nationalBook, self).__init__(**kwargs)

class internationalBook(Book):
    def __init__(self, **kwargs):
        self.internationalFlag = True
        self.dollarPrice = round(CurrencyRates().get_rate('USD', 'BRL'), 2)
        self.taxes = 40/100
        self.dolarRateWithTaxes = self.dollarPrice*(1+self.taxes)
        super(internationalBook, self).__init__(**kwargs)

    #@overides from Book.getTotalValue(self)
    def getTotalValue(self):
        return self.dolarRateWithTaxes*super(internationalBook, self).getTotalValue()