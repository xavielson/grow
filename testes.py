import alarm





# hora_liga=18
# hora_desliga=3
# hora_atual=5



def check_led_state_on_start(relay, hora_liga, hora_desliga):
    
    lista = []

    y=1
    while y<3:
        x=1
        while x<25:
            lista.append(x)
            x += 1    
        y += 1
        hora_atual=13
    if hora_liga > hora_desliga:

        for i, j in enumerate(lista):
            if j == hora_liga:
                index_hora_liga = i
                break

        for i, j in enumerate(lista):
            if j == hora_desliga:
                index_hora_desliga = i

        x = index_hora_liga

        while x < index_hora_desliga:
            if lista[x] == hora_atual:
                print("liga luz")
            else:
                pass
            x += 1

    if hora_liga < hora_desliga:

        if hora_atual > hora_liga and hora_atual < hora_desliga:
            print("liga luz")

check_led_state_on_start(alarm.led_vega, 18, 12)


