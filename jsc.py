import tkinter as tk
from tkinter import ttk

# Fonction pour calculer les frais de douane
def calculer_frais():
    valeur_marchandise = float(valeur_entry.get())
    cout_transport = float(transport_entry.get())
    assurances = float(assurances_entry.get())
    type_envoi = type_envoi_var.get()
    origine = origine_var.get()
    
    # Seuils de franchise et taux hypothétiques pour les droits de douane et la TVA
    seuil_franchise_particulier = 45 if origine != "UE" else 400
    seuil_franchise_commercial = 150
    taux_douane = 0.10  # 10% pour les droits de douane
    taux_tva = 0.20  # 20% pour la TVA
    
    # Calcul de la valeur totale de l'envoi
    valeur_totale = valeur_marchandise + cout_transport + assurances
    
    # Initialisation des frais
    frais_douane = 0
    frais_tva = 0
    
    # Vérification de l'exonération et calcul des frais selon le type d'envoi
    if type_envoi == "Particulier" and valeur_totale > seuil_franchise_particulier:
        frais_douane = (valeur_totale - seuil_franchise_particulier) * taux_douane
        frais_tva = (valeur_totale - seuil_franchise_particulier) * taux_tva
    elif type_envoi == "Commercial" and valeur_totale > seuil_franchise_commercial:
        frais_douane = (valeur_totale - seuil_franchise_commercial) * taux_douane
        frais_tva = (valeur_totale - seuil_franchise_commercial) * taux_tva
    
    total_frais = frais_douane + frais_tva
    
    # Affichage des frais calculés
    resultat_label.config(text=f"Frais de douane et TVA estimés: {total_frais:.2f} euros")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Calculateur de Frais de Douane")

# Variables
type_envoi_var = tk.StringVar()
origine_var = tk.StringVar()

# Widgets pour l'entrée des données
tk.Label(window, text="Valeur marchandise (€):").grid(row=0, column=0)
valeur_entry = tk.Entry(window)
valeur_entry.grid(row=0, column=1)

tk.Label(window, text="Coût transport (€):").grid(row=1, column=0)
transport_entry = tk.Entry(window)
transport_entry.grid(row=1, column=1)

tk.Label(window, text="Assurances (€):").grid(row=2, column=0)
assurances_entry = tk.Entry(window)
assurances_entry.grid(row=2, column=1)

tk.Label(window, text="Type d'envoi:").grid(row=3, column=0)
type_envoi_combo = ttk.Combobox(window, textvariable=type_envoi_var, values=["Particulier", "Commercial"], state="readonly")
type_envoi_combo.grid(row=3, column=1)
type_envoi_combo.current(0)  # Sélection par défaut

tk.Label(window, text="Origine de l'envoi:").grid(row=4, column=0)
origine_combo = ttk.Combobox(window, textvariable=origine_var, values=["UE", "DOM", "Pays tiers"], state="readonly")
origine_combo.grid(row=4, column=1)
origine_combo.current(0)  # Sélection par défaut

tk.Button(window, text="Calculer", command=calculer_frais).grid(row=5, columnspan=2)

resultat_label = tk.Label(window, text="Frais de douane et TVA estimés: ")
resultat_label.grid(row=6, columnspan=2)

# Lancement de l'application
window.mainloop()