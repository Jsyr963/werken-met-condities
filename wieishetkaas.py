if input("Is de kaas geel ? Ja of Nee : ") == 'Ja' :
    if input("Zitten er gaten in ? Ja of Nee : ") == 'Ja' :
        if input("Is de kaas belachelijk duur ? Ja of Nee : ") == 'Ja' :
            print("Emmenthaler")
        else:
            print("Leerdammer")    
    elif input("Is de kaas hard als steen ? Ja of Nee : ") == 'Ja' :
           print("Parmiggiano Reggiano")
    else:
           print("Goudse Kaas")
else:
    if input("Heeft de kaas blauwe schimmel ? Ja of Nee : ") == 'Ja' :
        if input("Heeft de kaas een korst ? Ja of Nee : ") == 'Ja' :
            print("Blue de Rochbaro")
        else:
            print("Foume d'Ambert")
    else:
        if input("Heeft de kaas een korst ? Ja of Nee : ") == 'Ja' :
            print("Camembert")
        else:
            print("Mozzerella")

