#DEVELOPED METE EKER
print("! VERSION 1.0 !")
import random
dsyad = str()
pcad  = str()
print("Write here .txt filename (ex:mypassword , metepassword , xxx) : ")
dsyad = str(raw_input())
print("Write here .txt file`s location (ex:/home/mete/Documents/ , C/Users/Dokument) : ")
knm = str(raw_input())
dosya = open(knm + dsyad +'.txt', 'a')
txt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','z','x','w']
print("1-  numbers + letters")
print("2-  letters + numbers")
print("3-  letters -and numbers mix")
print("Your choice ( 1 or 2 or 3) : ")
scm=int(input())
if(scm == 1):
    print ("How many makes password ? :")
    s = int(input())
    print("How many makes numbers : ")
    sys= int(input())
    print("How many makes letters : ")
    hrfs= int(input())
    txm1 = 1
    txm = 1
    x = 1
    while x <=s:
        txm1 = 1
        txm  = 1
        while txm1 <= sys:
            txm1 +=1
            y = random.randint(0 , 9)
            dosya.write(str(y))
        while txm <= hrfs:
            txm +=1
            y1 =random.choice(txt)
            dosya.write(str(y1))
        dosya.write("\n")
        a1 = 100 * x
        yzd = a1 /s
        print "%", yzd
        x+=1
if(scm == 2):
    print ("How many makes password ? :")
    s = int(input())
    print("How many makes numbers : ")
    sys= int(input())
    print("How many makes letters : ")
    hrfs= int(input())
    txm1 = 1
    txm = 1
    x = 1
    while x <=s:
        txm1 = 1
        txm  = 1
        while txm <= hrfs:
                txm +=1
                y1 =random.choice(txt)
                dosya.write(str(y1))
        while txm1 <= sys:
            txm1 +=1
            y = random.randint(0 , 9)
            dosya.write(str(y))
        dosya.write("\n")
        a1 = 100 * x
        yzd = a1 /s
        x +=1
        print "%",yzd
if(scm == 3):
    x = 1
    print ("How many makes password  :")
    s = int(input())
    ttt=1
    print("How many password include character : ")
    ttm = int(input())
    while x <=s:
        ttt=1
        while ttt <= ttm:
            ttt += 1
            y = random.randint(0 , 9)
            y1 =random.choice(txt)
            krsscm = random.choice((str(y) , str(y1)))
            dosya.write(str(krsscm))
        dosya.write("\n")
        a1 = 100 * x
        yzd = a1 /s
        print "%",yzd
        x +=1
dosya.close()
print("PASSWORD MAKE COMPLATED")
