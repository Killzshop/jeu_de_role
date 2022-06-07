import random
import os

reset = "o"
potion = 0
attaque_phrase = ["sort une ENORME HACHE et frappez fort sans trop visé mais sent qu'il touche son ennemi !", "fouille dans ses poches, ne trouve rien d'autre qu'une crotte de nez et la jette en plein visage de son ennemi", "Attrape son épée habituel envoie un coup et touche son ennemi"]
# print(random.choice(number_list))

while reset == "o":
    os.system('cls')
    print("\nRegles du jeu : Gagnez le combat contre votre adversaire, vous avez 3 potions a votre disposition.")
    pseudo = input("\nQuel es ton pseudo jeune aventurier ? ")
    potion_joueur_1 = 3
    pdv_joueur_1 = 50
    pdv_ennemis = 50
    while pdv_ennemis or pdv_joueur_1 >= 0:
        print(f"\n{pseudo} [{pdv_joueur_1}] PV || Ennemi [{pdv_ennemis}] PV")
        q = input(f"\n{pseudo} voulez vous [1] ATTAQUER ou [2] PRENDRE UNE POTION ? ")
        if q == "1":
            attaque = random.randint(5,10)
            print(f"{pseudo} {random.choice(attaque_phrase)} qui perd {attaque} point de vie !")
            pdv_ennemis = pdv_ennemis - attaque
            if pdv_ennemis <= 0:
                break
            attaque = random.randint(5,15)
            print(f"\nVotre ennemi se defend, il vous enleve {attaque} points de vie")
            pdv_joueur_1 = pdv_joueur_1 - attaque
            if pdv_joueur_1 <= 0:
                    break
        elif q == "2":
            if potion_joueur_1 > 0:
                potion = random.randint(15,50)
                potion_joueur_1 = potion_joueur_1 - 1
                pdv_joueur_1 = pdv_joueur_1 + potion
                print(f"\nVotre potion de soin vous rend [{potion}] points de vie")
                attaque = random.randint(5,15)
                print(f"\nVotre ennemi se defend, il vous enleve {attaque} points de vie")
                pdv_joueur_1 = pdv_joueur_1 - attaque
                if pdv_joueur_1 <= 0:
                    break
            else:
                attaque = random.randint(5,10)
                print(f"\nVous n'avez plus de potion donc vous attaquez votre ennemi et vous lui enlevez {attaque} points de vie")
                pdv_ennemis = pdv_ennemis - attaque
                if pdv_ennemis <= 0:
                    break
                attaque = random.randint(5,15)
                print(f"\nVotre ennemi se defend, il vous enleve {attaque} points de vie")
                pdv_joueur_1 = pdv_joueur_1 - attaque
                if pdv_joueur_1 <= 0:
                    break
    if pdv_ennemis <= 0:
        print("\nVotre ennemi meurt dans votre derniere assault !")
        print("\nVous avez Gagné")
    else:
        print("\nVous avez perdu")
    reset = input("\nVoulez vous recommencez ? o/n : " )
print("A bientot")        
                