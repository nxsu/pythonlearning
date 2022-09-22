class bankacc(object):

    ##constructor
    def __init__(self, name, balance, number):
        self.accname = name
        self.accbalance = balance
        self.accnumber = number
    
    ##getters
    def get_accname(self):
        return self.accname
    def get_accbalance(self):
        return self.accbalance
    def get_accnumber(self):
        return self.accnumber
    
    ##setters
    def set_accname(self, name):
        self.accname = name
    def set_accbalance(self, balance):
        self.accbalance = balance
    def set_accnumber(self, number):
        self.accnumber = number

    def tostring(self):
        return self.get_accnumber() + " - " + self.get_accname() + " - $" + self.get_accbalance() + "\n"


