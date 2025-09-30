#Zigomar
import random


'''
#pseudocode 

if len(sac){>= 14} # if sac #rangement >=15 objet max sinon random.shuffle (1,2)
1. retire tous objet/nombre "b"
2. demande quel objet retirer

    
fin chasse_au_trésor
random.shuffle(sac) print ("mélange aléatoire des objet du sac")
random.choice(sac)  
if random.choice(sac) == random.shuffle(sac)
return print("Zigomar a deviner votre objet et vous remercie")
else print("GRRRRR")
sac = [ "potions_scintillantes","clés_mystérieuses","boules_brillantes","squelettes_miniatures"]

list.sort(sac)
'''

def sac(item):
    """

    """

# --- Fonctions ---

def afficher_sac(sac):
    print("\n Sac de Zigomar :")
    for i, obj in enumerate(sac, 1):
        print(f"{i}. {obj}")


def ajouter_objets(sac):
    nb = int(input("Combien d'objets voulez-vous ajouter ? "))
    for _ in range(nb):
        obj = input("Nom de l'objet : ").strip()
        sac.append(obj)
    while True:
         if len(sac) >= 15:
            print("\n😮 Zigomar regarde son sac... Il déborde ! Elle doit faire le tri.")

            mode = random.choice(['auto', 'manuel'])

            if mode == 'auto':
                print("🔮 Zigomar murmure : 'Je fais ça à ma façon... automatique !'")
                tri_automatique(sac)
            else:
                print("👀 Zigomar te fixe : 'C’est TOI qui choisis quoi retirer maintenant !'")
                tri_utilisateur(sac)

         else:
            break


def tri_automatique(sac):
    print(" Tri automatique : retrait des objets contenant un chiffre ou un 'b'")
    objets_retires = []
    sac[:] = [obj for obj in sac if not any(char.isdigit() or char == 'b' for char in obj)]
    # Cette ligne remplace le sac par une version nettoyée


def tri_utilisateur(sac):
    afficher_sac(sac)
    choix = int(input("Entrez le numéro de l'objet à retirer : ")) - 1
    if 0 <= choix < len(sac):
        obj = sac.pop(choix)
        print(f"{obj} retiré du sac.")


def lancer_quiz(sac):
    print("\n Jeu de devinette avec Zigomar !")
    afficher_sac(sac)
    random.shuffle(sac)
    objet_secret = random.choice(sac)
    devine = input("Zigomar, devine l'objet mystère : ").strip()
    while True:
        if devine == objet_secret:
            print("🎉 BRAVO ! Zigomar est ravie !")
        elif devine != (sac):
            print("cela n'est pas un objet du sac")
        else:
            print(f" GRRRR... ce n'était pas ça. C'était : {objet_secret}")
        break

def trier_sac(sac):
    sac.sort()
    print(" Sac trié alphabétiquement.")



if __name__ == "__main__":

    sac = ["potions_scintillantes", "clés_mystérieuses", "boules_brillantes", "squelettes miniatures"]

    print("Bienvenue à votre adventure Zigomar")
    while True:
        print("\n=== Menu de la chasse au trésor ===")
        print("1. Afficher le sac")
        print("2. Ajouter des objets")
        print("3. Finir la chasse au tresor")

        choix = input("Faites votre choix : ")

        if choix == "1":
            afficher_sac(sac)
        elif choix == "2":
            ajouter_objets(sac)
        elif choix == "3":
            lancer_quiz(sac)
            trier_sac(sac)
            print(" Au revoir, aventurier·e !")

            break
        else:
            print("Choix invalide. Réessayez.")


