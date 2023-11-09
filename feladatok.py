import random
import math

#Kérj be 1 páros számot a felhasználótól. (1 pont)
#Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)
print("1.feladat")
def feladat1():
    szam:str=(input("Adj meg egy páros számot:"))
    while not(szam % 2 ==0):
        szam=input("Ez nem páros páros számot adj meg egy páros számot :")
        print(f"{szam}")

#  Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot.
#Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!”

print("2.feladat")
def feladat2():
    i=1
    while i<14:
        szam:int=math.floor(random.random()*(150-10)+50)
        print(szam)
        i+=1

#Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot.
#Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
#Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor!
print("3.feladat")
def feladat3(text,n):
    if len(text)<n:
        print("nincs n karakter")
    else:
        print(f"{n}.karakter a'{text[n]}'")
        i=0
        while i !=3:
            print(text[n],())

#Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
#Hány nevet adott meg a felhasználó?
#A kiírás formája: „A felhasználó 12 nevet adott meg.”
print("4.feladat")
def feladat4():
    szamlalo=0
    i=0
    while i != '@':
        nev=str("Adj meg egy nevet")
        if nev == '@':
            i='@'
            szamlalo+=1
            print(f'A felhasználó {szamlalo-1}nevet adott meg')



