import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import json
import os

kivy.require('2.1.0')  # Assure-toi d'utiliser une version de kivy compatible

# Fichier de sauvegarde des données
DATA_FILE = "game_data.json"

class GameApp(App):
    def build(self):
        self.load_data()  # Charger les données existantes
        self.layout = BoxLayout(orientation='vertical')
        
        # Affichage de l'argent
        self.money_label = Label(text=f"Argent : {self.money} $")
        self.layout.add_widget(self.money_label)
        
        # Bouton pour gagner de l'argent
        self.earn_button = Button(text="Gagner de l'argent")
        self.earn_button.bind(on_press=self.gain_money)
        self.layout.add_widget(self.earn_button)
        
        # Bouton pour investir
        self.invest_button = Button(text="Investir (100$)")
        self.invest_button.bind(on_press=self.invest_money)
        self.layout.add_widget(self.invest_button)

        return self.layout

    def load_data(self):
        """Charge les données du jeu depuis un fichier JSON."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                self.money = data.get("money", 0)
                self.investment = data.get("investment", 0)
        else:
            self.money = 0
            self.investment = 0

    def save_data(self):
        """Sauvegarde les données du jeu dans un fichier JSON."""
        data = {
            "money": self.money,
            "investment": self.investment,
        }
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file)

    def gain_money(self, instance):
        """Ajoute de l'argent au joueur."""
        self.money += 10 + self.investment  # L'argent gagné augmente avec l'investissement
        self.update_money_label()
        self.save_data()

    def invest_money(self, instance):
        """Permet au joueur d'investir de l'argent."""
        if self.money >= 100:
            self.money -= 100
            self.investment += 1
            self.update_money_label()
            self.save_data()
            self.show_popup("Investissement réussi", "Tu as investi dans une amélioration.")
        else:
            self.show_popup("Pas assez d'argent", "Tu n'as pas assez d'argent pour investir.")

    def update_money_label(self):
        """Met à jour l'affichage de l'argent."""
        self.money_label.text = f"Argent : {self.money} $"

    def show_popup(self, title, message):
        """Affiche une popup avec un message."""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.6))
        popup.open()

if __name__ == '__main__':
    GameApp().run()
