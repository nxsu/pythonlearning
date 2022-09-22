from module.account import bankacc
from module.bank import bank

if __name__ == '__main__':
    testbank = bank('Bank of America', 'Texas')
    
    testacc1 = bankacc('Bob E', '1', '987654321')

    testacc2 = bankacc('John Mith', '9000', '123567489')
    
    testacc = bankacc('John Smith', '624', '123456789')
    print(testacc.tostring())
    testacc.set_accbalance('2000')
    testacc.set_accname('John Stiencvabevk')
    print(testacc.tostring())

    testbank.add_bankacc(testacc)
    testbank.add_bankacc(testacc2)
    testbank.add_bankacc(testacc1)

    print(testbank.tostring())