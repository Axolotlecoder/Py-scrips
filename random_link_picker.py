import random

# Lies alle Links aus einer Datei
def lade_links(dateipfad):
    with open(dateipfad, "r", encoding="utf-8") as f:
        return [zeile.strip() for zeile in f if zeile.strip()]

def zufälliger_link(links):
    return random.choice(links)

links = lade_links("links.txt")  # Datei mit Links

print("Drücke Enter, um einen zufälligen Link zu erhalten (oder tippe 'q' zum Beenden):")

while True:
    eingabe = input(">>> ")
    if eingabe.lower() == "q":
        print("Beendet.")
        break
    print("Zufälliger Link:", zufälliger_link(links))

