"""Simple example illustrating the package."""
from src.darlehenpy import darlehen

# Die Ausgabe kann man schöner machen ;)

# Rahmenbedinungen
DARLEHENSSUMME = 100000
ZINSSATZ = 4.1
LAUFZEIT = 10
SONDERTILGUNG = 5000

print(
    f"""Darlehensumme: {DARLEHENSSUMME} €
Zinssatz (p.a.): {ZINSSATZ} %
Laufzeit: {LAUFZEIT} Jahre
Sondertilung (p.a.): {SONDERTILGUNG}
"""
)

# Berechnung basierend auf einer Monatsrate
MONATSRATE = 500
print(f"Monatsrate: {MONATSRATE} €")
TILGUNGSRATE, restschuld, gesamtaufwand, jahr, monat = darlehen.berechne_mit_monatsrate(
    DARLEHENSSUMME, ZINSSATZ, MONATSRATE, LAUFZEIT, SONDERTILGUNG
)
print(
    f"""Anfängliche Tilgungsrate: {TILGUNGSRATE} %
Restschuld nach {LAUFZEIT} Jahren: {restschuld} €
Gesamtaufwand: {gesamtaufwand} €
"""
)

# Berechnung basierend auf der anfänglichen Tilgungsrate
TILGUNGSRATE = 5.5
print(f"Anfängliche Tilgungsrate: {TILGUNGSRATE} %")
MONATSRATE, restschuld, gesamtaufwand, jahr, monat = darlehen.berechne_mit_tilgungsrate(
    DARLEHENSSUMME, ZINSSATZ, TILGUNGSRATE, LAUFZEIT, SONDERTILGUNG
)
print(
    f"""Monatsrate: {MONATSRATE} €
Restschuld nach {LAUFZEIT} Jahren: {restschuld} €
Gesamtaufwand: {gesamtaufwand} €
Abbezahlt im {monat}. Monat des {jahr}. Jahres
"""
)
