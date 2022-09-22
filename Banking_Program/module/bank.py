from module.account import bankacc

class bank(object):
    
    ##constructor
    def __init__(self, name, location):
        self.bankname = name
        self.banklocation = location
        self.bankaccs = []
    
    ##getters
    def get_bankname(self):
        return self.bankname
    def get_banklocation(self):
        return self.banklocation
    def get_bankaccs(self):
        return self.bankaccs

    ##setters
    def set_bankname(self, name):
        self.bankname = name
    def set_banklocation(self, location):
        self.banklocation = location
    def set_bankaccs(self, bankacclist):
        self.bankaccs = bankacclist
    
    def add_bankacc(self, acc):
        self.bankaccs.append(acc)
    
    def tostring(self):
        bank_ret = self.get_bankname() + ' - ' + self.get_banklocation() + ':\n'
        for account in self.bankaccs:
            bank_ret += '\t' + account.tostring()
        return bank_ret