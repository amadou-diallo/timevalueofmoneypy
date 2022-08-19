
import locale

def getAmount(prompt):
    a = -1
    while a <= 0:
        try:
            a = float(input(prompt))
            if (a <= 0):
                print("Positive values Only.")
        except ValueError:
            print("illegal entry : positive numeries only.")
        
    return a
    

def getTerm():
    t = -1
    while t < 0:
        try:
            t = int(input("Enter the Term (in months): "))
            if (t < 0):
                print(" A positive integer is required here. Please re-enter.")
        except ValueError:
            print(" Wrong data types entries, Integers Only Please.")
    return t


def doFV():
    amount = getAmount("Intial Deposit: ")
    rate = getAmount("Annual Interest Rate(6% = 6): ")
    while rate < 1.0 or rate > 25.0:
        print("Rate is out of bounds: 1 _ 25 % Only Please.")
    trm = getTerm()

    mothrate = rate/ 12.0/ 100.0
    fv = 0.0
    fv = amount * (1 + mothrate)** trm
    print("A deposit of %s" % locale.currency(amount,grouping=True)
          + " earning "
          + " {:.2%}".format(rate/100.0)
          + " annually for " + str(trm) + " months"
          + " will have a final value of: %s" % locale.currency(fv,grouping=True))
    print("That includes interest earned of %s"
          % locale.currency((amount-fv),grouping=True))
   
    

def doPV():
    amount = getAmount("A amount to be received: ")
    rate = getAmount("Annual Interest Rate (6% = 6): ")
    while rate < 1.0 or rate > 25.0:
        print("Rate is out of bounds: 1 - 25 % Only. ")
    trm = getTerm()

    monthrate = rate /  12.0/ 100.0
    pv = 0.0
    pv = amount / (1 + monthrate)** trm
    
    print("An amount of %s" % locale.currency(amount,grouping=True)
          + " to be received in " + str(trm) + " months"
          + " with an annual cost of money of %s" + " {:.2%}".format(rate/100.0)
          + " has a value today of: %s" % locale.currency(pv,grouping=True))
    print("That includes a discount of %s"
          % locale.currency((amount-pv),grouping=True))
    print()
    

    
    
def doFVA():
    amt = getAmount("Monthly Deposit: ")
    rate = getAmount("Annual Interest Rate (6.5% = 6.5): ")
    while rate < 1.0 or rate > 25.0:
        print("Rate is out of bounds: 1 - 25 % Only.")
        rate = getAmount("Annuel Interest Rate (6.5% = 6.5): ")
    term = getTerm()

    #formula requires monthly rate
    morate = rate/ 12.0/ 100.0
    fva = 0.0
    for i in range(0,term):
        intearn = (fva + amt) * morate
        fva += (intearn + amt)
    print("A monthly deposit of %s" % locale.currency(amt,grouping=True)
          + " earning "
          + " {:.2%}".format(rate/100.0)
          + " annually after " + str(term) + " months"
          + " will have a final value of: %s" % locale.currency(fva,grouping=True))
    print("That includes interest earned of %s"
          % locale.currency( (fva -(amt*term)),grouping=True))
   
    print()
        

def getChoice():
    c = -1
    while c < 0 or c > 3:
        try:
           c = int(input("Select Operation: 1 =PV, 2=FV, 3=FVA, 0=Quit): "))
           if c < 0 or c > 3:
                print("Unknown operation: 1-3 or zero only.")
        except ValueError:
             print("Illegal input: integers from 0 to 3 only.")
    return c
 
def main():
    #set the locale for use in currency formatting
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')

    choice = getChoice()
    while choice != 0:
        print()
        if choice == 1:
            doPV()
        elif choice == 2:
            doFV()
        elif choice == 3:
            doFVA()
        else:
            print("Unknown operation / not yet implented. \n")

        choice = getChoice() 
    print("Thanks for Using the Financial Calculator.")
    


if __name__ == "__main__":
    main()
