""" o _ o _ _ _ o _ e e """
"""
1. Iau prima si ultima litera, le afisez peste tot unde apar in cuvant iar restul  le ascund
1. Se cere utilizatorului sa introduca o litera mica
2. Avem un total de incercari egal cu numarul de _ de gasit
3. Daca a mai incercat litera respectiva, nu ii scad din vieti
"""


cuvant_initial = "abecedar"
cuvinte_incercate = {cuvant_initial[0], cuvant_initial[-1]}
display_cuvant = ["_" for val in cuvant_initial]
incercari_bonus = 1
is_game_over = False


def update_display_cuvant(cuvant_display, cuvant_initial, litere_incercate):
    for index, val in enumerate(cuvant_initial):
        if val in litere_incercate:
            cuvant_display[index] = val


def update_game_state():
    global incercari_ramase
    global is_game_over

    if incercari_ramase == 0 or "_" not in display_cuvant:
        is_game_over = True


def citeste_litera():
    global cuvinte_incercate
    global incercari_ramase

    litera_citita = input("Introduceti o litera mica: ")

    while litera_citita.isupper() or (litera_citita in cuvinte_incercate):
        print(f"Litere incercate: {cuvinte_incercate}")
        litera_citita = input("Introduceti o litera mica diferita de cele anterioare: ")
    cuvinte_incercate.add(litera_citita)

    return litera_citita


update_display_cuvant(display_cuvant, cuvant_initial, cuvinte_incercate)
incercari_ramase = len(['_' for val in display_cuvant if val == "_"]) + incercari_bonus

print(f"Viata ramasa: {incercari_ramase}\n\tCuvant: {' '.join(display_cuvant)}")

while not is_game_over:
    litera = citeste_litera()
    incercari_ramase -= 1
    cuvinte_incercate.add(litera)

    update_display_cuvant(display_cuvant, cuvant_initial, cuvinte_incercate)
    update_game_state()

    print(f"Viata ramasa: {incercari_ramase}\n\tCuvant: {' '.join(display_cuvant)}")


spatii_ramase = len(['_' for val in display_cuvant if val == "_"])
if spatii_ramase == 0:
    print("Felicitari, ai castigat!")
else:
    print("Ai pierdut :(")
