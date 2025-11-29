import Game_data.Programmes.Base_Fonction as Base_Fonction

import random
import time
import os



class main():
    def __init__(self):
        pass
    
    def charger_game(self, Partie_name):
        Game_dict = Base_Fonction.charger_dictionnaire(f"Game_data/Parties/{Partie_name}/game_data.json")
        return Game_dict
    
    def create_game(self):
        Parties = os.listdir("Game_data/Parties")
        user_input = ""
        while True:
            user_input = input("Entrez le nom de sauvgarde de la partie : ")
            if user_input in Parties:
                print("Cette sauvgarde existe déjà.")
            elif user_input == "":
                print("Veuillez entrer un nom valide.")
            else:
                try:
                    os.makedirs(f"Game_data/Parties/{user_input}", exist_ok=True)
                    break
                except:
                    print("Essayer de créer un nom de sauvegarde sans caractère spéciaux")
        
        Partie_name = user_input
        Partie_seed = random.randint(1, 10**9)

        Game_dict = {
            "game_name": Partie_name,
            "seed": Partie_seed,
            "last_update": time.time()
            }
        
        Base_Fonction.sauvegarder_dictionnaire(Game_dict, f"Game_data/Parties/{Partie_name}/game_data.json")

        print("Code pour rejoindre la partie : " + Base_Fonction.encode_number(Partie_seed))
        input("Appuyez sur entrée pour continuer...")

        return Game_dict
    
    def join_game(self):
        user_input = ""
        while True:
            user_input = input("Entrez le code de la partie : ")
            try:
                Partie_seed = Base_Fonction.decode_number(user_input)
                break
            except:
                print("Veuillez entrer un code valide.")

        Parties = os.listdir("Game_data/Parties")
        user_input = ""
        while True:
            user_input = input("Entrez le nom de sauvgarde de la partie : ")
            if user_input in Parties:
                print("Cette sauvgarde existe déjà.")
            elif user_input == "":
                print("Veuillez entrer un nom valide.")
            else:
                try:
                    os.makedirs(f"Game_data/Parties/{user_input}", exist_ok=True)
                    break
                except:
                    print("Essayer de créer un nom de sauvegarde sans caractère spéciaux")
        
        Partie_name = user_input

        Game_dict = {
            "game_name": Partie_name,
            "seed": Partie_seed,
            "last_update": time.time()
            }
        
        Base_Fonction.sauvegarder_dictionnaire(Game_dict, f"Game_data/Parties/{Partie_name}/game_data.json")

        return Game_dict
    
    def main(self):

        print('Version: 2.0.38.' + str(random.randint(0, 100)), '\t\t\tV2')
        print('                        ¤ Bienvenue ¤')
        print('')
        print('      Trader Game Life est un jeu de simulation')
        print("         d'investissement et de trading.")
        print('')
        print('   Achetez, vendez et gérez vos actifs pour devenir')
        print('            le maître du marché financier !')
        print('')

        if os.listdir("Game_data/Parties") == []:
            user_choice = None
            while not user_choice in ["1", "2"]:
                print("1. Créer une partie")
                print("2. Rejoindre une partie")
                user_choice = input("Choisissez une option : ")
                if not user_choice in ["1", "2"]:
                    print("Choix invalide. Veuillez réessayer.")
            
            if user_choice == "1":
                return self.create_game()
            elif user_choice == "2":
                return self.join_game()
        else:
            user_choice = None
            while not user_choice in ["1", "2", "3"]:
                print("1. Continuer la partie la plus récente")
                print("2. Créer une partie")
                print("3. Rejoindre une partie")
                user_choice = input("Choisissez une option : ")
                if not user_choice in ["1", "2", "3"]:
                    print("Choix invalide. Veuillez réessayer.")
            
            if user_choice == "1":
                Partie_most_recente = ["", 0]
                for Partie in os.listdir("Game_data/Parties"):
                    last_update = Base_Fonction.charger_dictionnaire(f"Game_data/Parties/{Partie}/game_data.json")["last_update"]
                    if last_update > Partie_most_recente[1]:
                        Partie_most_recente = [Partie, last_update]
                return self.charger_game(Partie_most_recente[0])
            elif user_choice == "2":
                return self.create_game()
            elif user_choice == "3":
                return self.join_game()