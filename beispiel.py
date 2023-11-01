import src.darlehenpy.darlehen as darlehen

# Die Ausgabe kann man schöner machen ;)

# Rahmenbedinungen
P = 100000
i = 4.1
n = 10
S = 5000

print(
    f"Darlehensumme: {P} €\nZinssatz (p.a.): {i} %\nLaufzeit: {n} Jahre\nSondertilung (p.a.): {S}\n"
)

# Berechnung basierend auf einer Monatsrate
M = 500
print(f"Monatsrate: {M} €")
t0, R, gesamtaufwand, jahr, monat = darlehen.berechne_mit_monatsrate(P, i, M, n, S)
print(
    f"Anfängliche Tilgungsrate: {t0} %\nRestschuld nach {n} Jahren: {R} €\nGesamtaufwand: {gesamtaufwand} €\nAbbezahlt im {jahr}. Jahr und {monat}. Monat\n"
)

# Berechnung basierend auf der anfänglichen Tilgungsrate
t0 = 5.5
print(f"Anfängliche Tilgungsrate: {t0} %")
M, R, gesamtaufwand, jahr, monat = darlehen.berechne_mit_tilgungsrate(P, i, t0, n, S)
print(
    f"Monatsrate: {M} €\nRestschuld nach {n} Jahren: {R} €\nGesamtaufwand: {gesamtaufwand} €\nAbbezahlt im {jahr}. Jahr und {monat}. Monat"
)
