from domande import Domande

import random

f = open("domande.txt", "r").read().splitlines()
d = []

for q in range(0, len(f), 7):
    d.append(Domande(domanda=f[q], difficolta=f[q+1], risposta= f[q+2], opzioni=f[q+2:q+6]))

diff=0
max_diff= max(d, key =lambda x: x.difficolta).difficolta

dnow = []

for x in d:
    if int(x.difficolta)==diff:
        dnow.append(x)

i = random.randint(0, len(dnow)-1)
opzioniNow = dnow[i].opzioni_random()
rispostaNow = dnow[i].risposta
diifNow =dnow[i].difficolta
domandaNow = dnow[i].domanda

print("Livello " + diifNow + ". Domanda: " + domandaNow)


