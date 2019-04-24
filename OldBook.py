print("Bienvenue chez OLD BOOK! Utilisez le menu pour nous dire ce que vous voulez faire :")

class Client:

    def __init__(self, nom, credit):
        self.nom = nom
        self.credit = int(credit)

    def affichage(self):
        print("""
        Credit du client {} : {}""".format(self.nom, str(self.credit)))

    def crediter(self, credit):
        self.credit += credit



class Livre:

    def __init__(self, titre, prix, auteur, style):

        self.titre = titre
        self.prix = prix
        self.auteur = auteur
        self.style = style
        self.stock = 0

    def approvisionnement(self, quantitel):
        self.stock += quantitel

    def affichage(self):

        print("""
        Titre de l'ouvrage : {}
        Prix unitaire : {}
        Auteur : {}
        Style : {}
        Stock du livre : {}
        """.format(self.titre, str(self.prix), self.auteur, self.style, str(self.stock)))



class OldBook:

    def __init__(self, clients=[], livres=[]):

        self.livres = livres
        self.clients = clients

    def ajoutclient(self, client):
        self.clients.append(client)


    def __lireClient(self):

        trouve = False
        while not trouve:
            client = input("Quel est le nom du client? ")
            for unclient in self.clients:
                if unclient.nom == client:                      # == en algebre veut dire "<--". Elle affecte une valeure à une variable.
                    trouve = True
                    break
            if not trouve:
                print("Ce Client n'existe pas")
        return unclient

    def __lireLivre(self):

        trouve = False
        while not trouve:
            livre = input("Quel est le titre de l'ouvrage? ")
            for unlivre in self.livres:
                if unlivre.titre == livre:
                    trouve = True
                    break
            if not trouve:
                print("Ce livre n'existe pas")
        return unlivre

    def achat(self):

        unclient = self.__lireClient()
        unlivre = self.__lireLivre()
        paiement = -1
        while paiement == -1:
            paiement = input("Quel est le montant du paiement? ")
            try:                                        # le bloc try/except/finally permet de tester un programme.
                paiement = int(paiement)                # "try" est un bloc que le programme va executer.
                assert paiement >= 0                    # S'il fonctionne python va executer la suite, sinon il execute le bloc "except".
            except ValueError:                          # Le bloc finally est exécuté quelque soit le resultat du bloc.
                print("Rentrer un montant valide")
            except AssertionError:
                print("Rentrer un montant positif")
                paiement = -1

        quantite = -1
        while quantite == -1:
            quantite = input("Quel est la quantité souhaité? ")
            try:
                quantite = int(quantite)
                assert quantite >= 0                            #Les assertions sont un moyen de s'assurer, avant de continuer, qu'une condition est respectée.
            except AssertionError:                              # Si elle n'est pas respectée, elle affiche "AssertionError"
                print("Rentrer une quantité positive")          # Avec un print on peut afficher la chaine de caractere voulue.
                quantite = -1
            except ValueError:
                print("Rentrer une quantité valide")

        unlivre.stock -= quantite
        unclient.credit = unlivre.prix * quantite - paiement


    def approvisionnement(self):

        unlivre = self.__lireLivre()
        quantite = -1
        while quantite == -1:
            quantite = input("Donner la quantité? ")
            try:
                quantite = int(quantite)
                assert quantite >= 0
            except AssertionError:
                print("Rentrer une quantité positive")
                quantite = -1
            except ValueError:
                print("Rentrer une quantité valide")
        unlivre.stock += quantite


    def affichage(self):

        for elt in self.clients:
            elt.affichage()

        for elt in self.livres:
            elt.affichage()



def quitter():
    print("""
    Programme terminé. Merci de votre visite et à bientôt!""")
    exit(0)

def menu():
    print("""
1 : Approvisionner le stock d'un livre existant
2 : Ajouter un client
3 : Vérifier l'états des stocks et des credits
4 : Acheter un livre
5 : Quitter""")

    while True:
        try:
            choix = int(input("Entrez votre choix: "))
            if choix in range(1, 6):
                return choix
        except ValueError:
            continue

Jelis = Client("Jelis",0.0)
Jebouquine = Client("Jebouquine",0.0)

NotreDamedeParis = Livre("NotreDamedeParis", 20, "VH", "roman")
Leroutard = Livre("Leroutard", 19, "GDR", "guide")

clients = [Jelis, Jebouquine]
livres = [NotreDamedeParis, Leroutard]

oldBook = OldBook(clients, livres)
while True:

    choix = menu()

    if choix == 1:
        oldBook.approvisionnement()
    elif choix == 2:
        clientName = str(input("Quel est le nom du nouveau client ?"))
        clientCredit = int(input("Quel est son credit ?"))
        client = Client(clientName, clientCredit)
        oldBook.ajoutclient(client)
    elif choix == 3:
        oldBook.affichage()
    elif choix == 4:
        oldBook.achat()
    elif choix == 5:
        quitter()
    else:
        break

