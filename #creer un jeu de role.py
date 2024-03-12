#creer un jeu de role
import sys ; import random 
point_vie=point_vie_ennemi=50
nb_potion=3
choix_possible=["1" , "2" ]
print("\u2694 C'EST L'HUEURE DU DUEL \u2694")

while True:
    choix=input("*****Voulez-vous attaquer(1) ou vous soigner(2)?*****\n")
    if  choix not in choix_possible:
        print("votre choix est invalide!!! reessayer ")
        continue
    if choix=="1":
        point_vie_ennemi=point_vie_ennemi-random.randint(5,10)
        if point_vie_ennemi<=0:
            print(' Le jeu est termine. vous etes le vainqueur!! ')
            sys.exit()
        else:
            point_vie=point_vie-random.randint(5,15)
            if point_vie<=0:
                print(" Le jeu est termine. votre opposant est le vainqueur!!?? ")
                sys.exit()
            else:
                print(f"vous attaquez,il reste {point_vie_ennemi} PV à votre opposant. votre opposant attaque, il vous reste {point_vie} PV ")
    if choix=="2":
        if point_vie>=50:
            print("vos PV sont au maximum!!! vous ne pouvez pas prendre de potion")
            continue
        elif nb_potion<=0:
             print("**Vous n'avez plus de potions!! Impossible de se soigner**")
             continue
        elif point_vie<50:
            point_vie=point_vie+random.randint(15,50)
            if point_vie>50:
                point_vie=50
                print(f"**vos PV sont au maximum!!!**")
            elif point_vie<50:
                 print(f"**vous avez maintenant {point_vie} PV**")
            nb_potion=nb_potion-1
            if nb_potion<=0:
                    print(f"**il ne vous reste plus de potions de soins !!!**")
            else   :
                    print(f"**il vous reste {nb_potion} potions de vies!**")
        point_vie=point_vie-random.randint(5,15)
        print(f"il reste {point_vie_ennemi} PV à votre opposant. votre opposant attaque, il vous reste {point_vie} PV ")
        print("***vous passez votre tour***")       
        point_vie=point_vie-random.randint(5,15)
        print(f"il reste {point_vie_ennemi} PV à votre opposant. votre opposant attaque, il vous reste {point_vie} PV ")