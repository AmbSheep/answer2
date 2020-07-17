#!/usr/bin/env python3
import sys
def countChange(amount):
    return cc(amount, 3)
def cc(amount, kindsOfCoins):
    if amount==0:
        return 1
    if amount<0 or kindsOfCoins==0:
        return 0
    else:
        return cc(amount, kindsOfCoins-1)+cc(amount-firstDenomination(kindsOfCoins), kindsOfCoins)
def firstDenomination(kindsOfCoins):
    if kindsOfCoins==1:
        return 1
    elif kindsOfCoins==2:
        return 3
    else:
        return 5
if __name__=='__main__':
    print(countChange(sys.argv[1]))