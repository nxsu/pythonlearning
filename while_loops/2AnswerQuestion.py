## test for typing etc. also a refresher. this is my first .py document in like 3 months.

## attempt at user question i guess

def pineappleQuestion():
    while True:
        ## defines 'userinput' as the answer to the question of pineapple pizza and then capitalizes it.
        userinput = str.upper(input('hey, is pinapple on pizza good? (Y,N)\n>>'))
        if userinput == 'Y' or userinput == 'N':
            match userinput:
                case 'Y':
                    return 'eat shit you nasty swine'
                case 'N':
                    return ':D'
        else:
            print('wtf? try again')

## prints the returned value of the function 'pineappleQuestion'
print(pineappleQuestion())

## this actually turned out pretty alright, refreshed match case knowledge and i actually cleaned it up



