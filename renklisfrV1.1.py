#METE EKER
import random
import os
normal = '\033[0m'
kirmizi= '\033[31m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'#p --> parlak
pyesil = '\033[92m'
psari = '\033[93m'
siyah = '\033[90m'
asiyah= '\033[40m'#a --> arkaplan
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
print(akirmizi +siyah+"! VERSION 1.1 !"+normal)
dsyad = str()
pcad  = str()
print(pmavi+".txt uzantili dosya adini giriniz (Or: sifrem , sifre , psswrd) :")
dsyad = str(raw_input())
print(pmavi+".txt dosyasinin kaydedilicegi konumu girin  (Or: /home/user/Belgeler/ , C:/Belgeler/")
knm = str(raw_input())
dosya = open(knm + dsyad +'.txt', 'a')
txt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','z','x','w']
print(pyesil+"1-  sayi + harf")
print(pyesil+"2-  harf + sayi")
print(pyesil+"3-  harf - sayi karisik")
print(pyesil+"Seciminiz (1 , 2 ya da 3) : "+normal)
scm=int(input())
if(scm == 1):
    print (pmavi+"Kac tane sifre olusturulsun ? :"+normal)
    s = int(input())
    print(pmavi+"Kac tane sayi olusturulsun : "+normal)
    sys= int(input())
    print(pmavi+"Kac tane harf olusturulsun : "+normal)
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
        os.system("clear")
        print psari +"%", str(yzd) + normal
        x+=1
if(scm == 2):
    print (pmavi+"Kac tane sifre olusturulsun ? :"+normal)
    s = int(input())
    print(pmavi+"Kac tane sayi olusturulsun : "+normal)
    sys= int(input())
    print(pmavi+"Kac tane harf olusturulsun : "+normal)
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
        os.system("clear")
        print psari +"%", str(yzd) + normal
if(scm == 3):
    x = 1
    print (pmavi+"Kac tane sifre olusturulsun ? :"+normal)
    s = int(input())
    print(pmavi+"Kac tane sayi olusturulsun : "+normal)
    sys= int(input())
    print(pmavi+"Kac tane harf olusturulsun : "+normal)
    hrfs= int(input())
    while x <=s:
        ttt=1
        
        while ttt <=s:
            ttt += 1
            y = random.randint(0 , 9)
            y1 =random.choice(txt)
            krsscm = random.choice((str(y) , str(y1)))
            dosya.write(str(krsscm))
        dosya.write("\n")
        a1 = 100 * x
        yzd = a1 /s
        os.system("clear")
        print psari +"%", str(yzd) + normal
        x +=1
dosya.close()
print(akirmizi +"SIFRE YAZIMI TAMAMLANDI"+normal)
