legume = "tomate"
qt_legume = input("combien de legumes?")
fruit = "pomme"
qt_fruit = input("combien de fruits?")

panier = {"patates", "tomates", "cerises"}
recette = {'patates':'4', 'tomates':'5', 'cerises':'6'}

# Transforme les quantités en integer
qt_legume = int(qt_legume)
qt_fruit = int(qt_fruit)

resultat = qt_fruit + qt_legume

print(panier)
print(recette)
print(f"Il y a {round(resultat, 2)} fruits et legumes dans le panier")