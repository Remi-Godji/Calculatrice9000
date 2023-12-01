historique = []

def calculatrice():
    try:
        nombre1 = float(input("veuillez entrez le premier nombre : "))
        nombre2 = float(input("veuillez entrez  le deuxième nombre : "))
        operateur = input("Entrez l'opérateur ( exemple : +, -, *, /) : ")

        if operateur == '+':
            resultat = nombre1 + nombre2
        elif operateur == '-':
            resultat = nombre1 - nombre2
        elif operateur == '*':
            resultat = nombre1 * nombre2
        elif operateur == '/':
            resultat = nombre1 / nombre2
        else:
            print("Opérateur ne marche pas veuillez entrez les operateurs  : '+', '-', '*', '/'")
            return

        operation = f"{nombre1} {operateur} {nombre2} = {resultat}"
        historique.append(operation)

        print("Le résultat de l'opération est :", resultat)

    except ValueError:
        print("Entrée invalide. Veuillez entrer des nombres valides.")
    except ZeroDivisionError:
        print("Erreur : division par zéro.")

def afficher_historique():
    print("Historique des opérations :")
    for operation in historique:
        print(operation)

def effacer_historique():
    historique.clear()
    print("L'historique a été effacé.")


calculatrice()
afficher_historique()
effacer_historique()