#Hoofdletter gevoelig
import time

print('''
███████╗██╗███████╗ █████╗     ██████╗ ██████╗ 
██╔════╝██║██╔════╝██╔══██╗    ╚════██╗╚════██╗
█████╗  ██║█████╗  ███████║     █████╔╝ █████╔╝
██╔══╝  ██║██╔══╝  ██╔══██║    ██╔═══╝ ██╔═══╝ 
██║     ██║██║     ██║  ██║    ███████╗███████╗
╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝    ╚══════╝╚══════╝
                                               ''')
def main():
    time.sleep(1)
    if input("De Jong heeft de bal 5 meter buiten de 16, pas je de bal naar Depay of Dest ?: ") == 'Dest' :
        time.sleep(1)
        print("De bal werd afgepakt en nu moet je terug sprinten naar je positie!")
        time.sleep(1)
    else:
        time.sleep(1)
        print("Je hebt de goede keuze gemaakt, nu staat Depay op de goede positie voor een voorzet of een korte pass!")
        time.sleep(1)
    if input("Depay staat rechts voor het doel buiten de 16, speel Depay een voorzet of een korte pass? korte pass of voorzet? :") == "korte pass" :
        time.sleep(1)
        print("Korte pass wordt onderschept en de tegenstander gaat op de counter!")
        time.sleep(1)
    else:
        time.sleep(1)
        print("de voorzet komt goed aan bij de eerste paal bij Fati!")
        time.sleep(1)
    if input("Fati kan de bal richting het doel koppen of passen naar zijn teamgenoot Coutinho, Passen of Koppen ? :") == "Koppen" :
        time.sleep(1)
        print("De keeper vangt de bal en gooit de bal snel naar zijn aanvaller en gaan op de Counter-Attack!")
        time.sleep(1)
    else:
        time.sleep(1)
        print("Coutinho neemt de bal aan en kijkt om zich heen voor pass mogelijkheden!")
        time.sleep(1)
    if input("Coutinho staat rechts voor het doel en kan schieten of een voorzet geven, voorzet of schieten? :") == "schieten" :
        time.sleep(1)
        print("Bijna! De bal komt op de lat en kaatst terug naar Dest links van het doel")
        time.sleep(1)
    else:
        time.sleep(1)
        print("De Keeper bokst de bal weg en de tegenstander heeft bal bezit!")
        time.sleep(1)
    if input("Dest heeft de bal op het middenveld en heeft een mogelijkheid om een afstandschot te nemen of te passen naar Puig, Passen of Afstandschot? :") == "Afstandschot":
       time.sleep(1)
       print("Domme keuze...Dest is geen aanvaller en zijn schot wordt zonder moeite geblokt!")
       time.sleep(1)
    else:
        time.sleep(1)
        print("Slimme keuze! Puig heeft nu veel ruimte om te kiezen naar welke speler hij wilt spelen!")
        time.sleep(1)
    if  input("Puig staat net buiten de 16, hij kan een lange pass terug spelen of een afstandschot nemen vanaf ongeveer 20 meter, Afstandschot of lange pass? :") == "lange pass":
        time.sleep(1)
        print("De lange pass landt precies goed op de voeten van Jordi Alba. Prachtig!")
        time.sleep(1)
    else:
        time.sleep(1)
        print("Helaas...het schot wordt zonder moeite tegen gehouden")
        time.sleep(1)
    if input("Jordi Alba kan een hoge bal spelen voor het doel om te koppen of een korte pass afspelen, hoge bal of korte pass ?: ") == "korte pass":
       time.sleep(1)
       print("Oh nee! de bal wordt onderschept door een verdediger en de tegenstander gaat op de counter-attack!")
       time.sleep(1)
    else:
        time.sleep(1)
        print("De voorzet komt net iets te kort waardoor een verdediger de bal achter het doel kopt en jij nu een corner hebt!")
        time.sleep(1)
    if input("je kan de corner lang of kort spelen, kort of lang ?: ") == "lang":
        time.sleep(1)
        print("de bal wordt heel makkelijk door de keeper gevangen en het aanval is gedoofd.")
        time.sleep(1)
    else:
        time.sleep(1)
        print("de bal wordt kort genomen naar De Jong!")
        time.sleep(1)
    if input("De jong kan een hoge bal spelen of kort afleggen op busquets, hoge bal of kort afleggen?: ") == "hoge bal":
        time.sleep(1)
        print("De bal is helaas in de lucht gevangen door de keeper!")
        time.sleep(1)
    else:
        time.sleep(1)
        print("de pass wordt goed geleverd aan Coutinho!")
        time.sleep(1)
    if input("Coutinho kan een mooie steek pass in de 16 afgeven aan Depay, passen of zelf schieten?: ") == "zelf schieten":
        time.sleep(1)
        print("Jammer...de bal wordt tegen gehouden")
        time.sleep(1)
    else:
        time.sleep(1)
        print("Depay neemt de bal perfect aan en kan afmaken! ")
        time.sleep(1)
    if input("Depay staat goed voor het doel om een schot te wagen, schieten of afleggen?: ") == "Schieten":
        return True

    return True
if __name__== "__main__":
    if main():
        time.sleep(1)
        print("Depay schoot de bal recht in de kruising en het publiek ging tekeer!")
    else:
        time.sleep(1)
        print("De bal werd afgepakt en de tegenstander ging op de counter-attack!")
