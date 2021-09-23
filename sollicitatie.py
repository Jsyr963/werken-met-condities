def main():
    if float(input("Hoeveel jaar praktijk ervarig heeft u met dieren-dressuur? : ")) <=4:
        if float(input("Hoeveel jaar ervaring heeft met jongleren? : ")) <= 5:
           if float(input("Hoeveel jaar praktijk ervarig heeft u met acrobatiek? : ")) <=3:
               return False

   
    if input("Heeft u een MBO-4 Diploma ondernemen? (Ja of Nee) : ") == "Nee":
        return False
        
    if input("Bent u in het bezit van een geldig rijbewijs ? (Ja of Nee) : ") == "Nee":
        return False
        
    if input("Bent u in het bezit van een hoge hoed ? (Ja of Nee) : ") == "Nee":
        return False
    
    if input("Bent u een Man of een Vrouw ? : ") == "Man":
        if float(input("Hoeveel cm breed is uw snor? :  ")) <= 9:
            return False
    else:
        if input("Is uw Haarkleur Rood ? (Ja of Nee) : ") == "Nee":
            return False
        if float(input("Hoelang is uw Haar in cm ? : ")) <= 19: 
            return False
    if float(input("Hoelang bent u in cm ? : ")) <= 149:
        return False
    if float(input("Hoeveel weegt u in KG? : ")) <= 89:
        return False
    if input("Bent u in het bezit van het certificaat ''Overleven met gevaarlijk personeel'' (Ja of Nee) : ") == "Nee":
        return False

    return True

if __name__== "__main__":
    if main():
        print("U bent hierbij uitgenodigd voor een intake gesprek!")
    else:
        print("Helaas... we kunnen uw diensten niet gebruiken op dit moment.")