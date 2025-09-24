import random
def oyun():
    yazı_tura=['yazı','tura']
    atılan=random.choice(yazı_tura)
    secım=input('seciminiz nedir')
    if secım ==atılan:

        print('kazandın')
    else:
        print('kaybettin')
oyun()