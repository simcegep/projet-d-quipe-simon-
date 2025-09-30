import random


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

    if len(sac) > 15:
        choix = input("Le sac est trop plein ! Tri automatique (a) ou manuel (m) ? ").lower()
        if choix == 'a':
            tri_automatique(sac)
        else:
            tri_utilisateur(sac)


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
    random.shuffle(sac)
    objet_secret = random.choice(sac)
    devine = input("Zigomar, devine l'objet mystère : ").strip()
    if devine == objet_secret:
        print("🎉 BRAVO ! Zigomar est ravie !")
    else:
        print(f" GRRRR... ce n'était pas ça. C'était : {objet_secret}")


def trier_sac(sac):
    sac.sort()
    print(" Sac trié alphabétiquement.")


# --- Programme principal ---
def main():
    sac = ["potions_scintillantes", "clés_mystérieuses", "boules_brillantes", "squelettes_miniatures"]

    while True:
        print("\n=== Menu de la chasse au trésor ===")
        print("1. Afficher le sac")
        print("2. Ajouter des objets")
        print("3. Lancer le quiz de Zigomar")
        print("4. Trier le sac")
        print("5. Quitter")

        choix = input("Faites votre choix : ")

        if choix == "1":
            afficher_sac(sac)
        elif choix == "2":
            ajouter_objets(sac)
        elif choix == "3":
            lancer_quiz(sac)
        elif choix == "4":
            trier_sac(sac)
        elif choix == "5":
            print(" Au revoir, aventurier·e !")
            break
        else:
            print("Choix invalide. Réessayez.")


if __name__ == "__main__":
    main()
