#DEVELOPED METE EKER
print("! VERSION 1.0 !")
import random
dsyad = str()
pcad  = str()
print(".txt uzantili dosya adini giriniz (Or: sifrem , sifre , psswrd) :")
dsyad = str(raw_input())
print(".txt dosyasinin kaydedilicegi konumu girin  (Or: /home/user/Belgeler/ , C:/Belgeler/")
knm = str(raw_input())
dosya = open(knm + dsyad +'.txt', 'a')
txt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','z','x','w']
print("1-  sayi + harf")
print("2-  harf + sayi")
print("3-  harf - sayi karisik")
print("Seciminiz (1 , 2 ya da 3) : ")
scm=int(input())
if(scm == 1):
    print ("Kac tane sifre olusturulsun ? :")
    s = int(input())
    print("Kac tane sayi olusturulsun : ")
    sys= int(input())
    print("Kac tane harf olusturulsun : ")
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
    print ("Kac tane sifre olusturulsun ? :")
    s = int(input())
    print("Kac tane sayi olusturulsun : ")
    sys= int(input())
    print("Kac tane harf olusturulsun : ")
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
    print ("Kac tane sifre olusturulsun ? :")
    s = int(input())
    ttt=1
    print("Sifre kac karakterli olsun : ")
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
print("SIFRE YAZIMI TAMAMLANDI")
