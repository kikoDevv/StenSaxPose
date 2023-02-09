import random
import time
program = True
körOm = True
playerScore = 0
datorScor = 0
ingenvann = 0

#func
#func till gamförelse av svar från player och dator och resultat av med som van
def vemVan (player, dator):
    if player <2 and dator >2:
        print("du har sten och dator har pose")
        time.sleep(2)
        print("👐DATOR VANN!!!👐")
        #return siffror är för att vi ska kunna räcka scores på vem som har vunnit mest. första siffran är player score andra är dator tredje är antalgånger ingen van
        return 0,1,0
    elif dator <2 and player >2:
        print("Du har pose vs Dator har sten")
        time.sleep(2)
        print("👐DU VANN!!👐")
        return 1,0,0
    elif player == dator +1:
        print("Du har",game[player]," VS Dator har",game[dator])
        time.sleep(2)
        print("👐DATOR VANN!!👐")
        return 0,1,0
    elif dator == player +1:
        print("Du har",game[player]," VS Dator har",game[dator])
        time.sleep(2)
        print("👐DU VANN!!👐")
        return 1,0,0
    elif player == dator:
        print("Du har",game[player],"VS Dator har",game[dator])
        print("KÖR OM")
        return 0,0,1


#fanc end
#func till huvudMeny
def huvudMney():
    print("↱----------------{VÄLKOMMEN}----------------↰")
    print("| [1] för att spela med dator               |")
    print("| [2] för att kolla dina scors              |")
    print("| [3] för att avsluta programmet            |")
    print("↳-------------------------------------------↲")
# func end
#func till graphic animation
def piler ():
    time.sleep(0.3)
    print(" ⇘ ")
    time.sleep(0.3)
    print("   ⇘")
    time.sleep(0.3)
    print("     ⇘")
    time.sleep(0.3)
    print("       ⇘")
    time.sleep(0.3)
    print("         ⇘")
    time.sleep(0.3)
    print("           ⇘ ")
    time.sleep(0.3)
    print("             ⇘")
    time.sleep(0.3)
    print("                ⇘")
    time.sleep(0.3)
    print("                  ⇘")
    time.sleep(0.3)
    print("                    ⇘")
    time.sleep(0.3)
    print("                      ⇘")
    time.sleep(0.3)
    print("                        ⇘")
    time.sleep(0.3)
    print("                           ⇘")
    time.sleep(0.3)
    print("                              ⇘")
    time.sleep(0.3)
    print("                                ⇘")
    time.sleep(0.3)
    print("                                  ⇘")
    time.sleep(0.3)
    print("                                    ⇘")
    time.sleep(0.3)
    print("                                       ⇘")
    time.sleep(0.3)
    print("                                          ⇘")
    time.sleep(0.3)
    print("                                            ⇘")
    time.sleep(0.3)
    print("                                               ⇘")
    time.sleep(0.3)
    print("                                                  ⇘")
    time.sleep(0.3)
    print("                                                     ⇘")
    time.sleep(0.3)
    print("                                                       ⇘")
    time.sleep(0.3)
    print("                                                         ⇘|")
    print("                                                         ⇙|")
    time.sleep(0.2)
    print("                                                      ⇙")
    time.sleep(0.2)
    print("                                                   ⇙")
    time.sleep(0.2)
    print("                                                ⇙")
    time.sleep(0.2)
    print("                                             ⇙")
    time.sleep(0.2)
    print("                                        ⇙")
    time.sleep(0.2)
    print("                                     ⇙")
    time.sleep(0.2)
    print("                                  ⇙")
    time.sleep(0.2)
    print("                              ⇙")
    time.sleep(0.2)
    print("                          ⇙")
    time.sleep(0.2)
    print("                     ⇙")
    time.sleep(0.2)
    print("                 ⇙")
    time.sleep(0.2)
    print("              ⇙")
    time.sleep(0.2)
    print("          ⇙")
    time.sleep(0.2)
    print("       ⇙")
    time.sleep(0.2)
    print("    ⇙")
    time.sleep(0.2)
    print("⇙")
#func ended
#func animation till scroll
def tumt():
    print("                                           ⇙|")
    time.sleep(0.2)
    print("                                         ⇙")
    time.sleep(0.2)
    print("                                       ⇙")
    time.sleep(0.2)
    print("                                     ⇙")
    time.sleep(0.2)
    print("                                   ⇙")
    time.sleep(0.2)
    print("                                 ⇙")
    time.sleep(0.2)
    print("                              ⇙")
    time.sleep(0.2)
    print("                            ⇙")
    time.sleep(0.2)
    print("                          ⇙")
    time.sleep(0.2)
    print("                       ⇙")
    time.sleep(0.2)
    print("                    ⇙")
    time.sleep(0.2)
    print("                ⇙")
    time.sleep(0.2)
    print("              ⇙")
    time.sleep(0.2)
    print("          ⇙")
    time.sleep(0.2)
    print("       ⇙")
    time.sleep(0.2)
    print("    ⇙")
    time.sleep(0.2)
    print("⇙")


#dictionary till sten sax pose för att kunna lätt översätta dem till siffra
game = {
    1 : "sten",
    2 : "sax",
    3 : "pose",
    "sten": 1,
    "sax": 2,
    "pose":3,
}
## START va programmet

while program:
    # HuvudMeny
    huvudMney()
    menyVal = 0
    körOm = True
    menyVal = input("👉 ")
    # Menyval 1
    if menyVal == "1":
        tumt()
        while körOm:
            felInput = True
            while felInput:
                print("↱-----------[skriv in ditt val]-----------↰")
                playerOrd = input("👉 ")
                if playerOrd == "sten" or playerOrd == "sax" or playerOrd == "pose":
                    playerSiffra = game[playerOrd]
                    felInput = False
                else:
                    print("❎Du har skrivit fel input, skriv: sten eller sax eller pose!")
                    time.sleep(3)
            datorSiffra = random.randint(1, 3)
            datorOrd = game[datorSiffra]
            # addera och spara return siffror från vemVan func för att see scores
            # p är playerScor, d är datorScore och i är ingenvann score
            p,d,i = vemVan(playerSiffra,datorSiffra)
            playerScore = p + playerScore
            datorScor = d + datorScor
            ingenvann = i + ingenvann
            print("↳-----------------------------------------↲")
            körOmInput = ""
            körOmInput = input("Vill du köra om?")
            if körOmInput == "ja" or körOmInput == "Ja":
                körOm = True
            elif körOmInput == "nej" or körOmInput == "Nej":
                print("huvud Meny...")
                körOm = False
            else: print("Fell input! svara ja eller nej")

        piler()
    elif menyVal == "2":
        print("↱-----------[SCORES]-----------↰")
        print("| Du har vunnit",playerScore,"gårner       |")
        print("| Dator vunnit",datorScor,"gånger        |")
        print("| ingen vann ", ingenvann, "               |")
        if playerScore > datorScor:
            print("↳-----(DU har vunnit mest)-----↲")
        elif datorScor > playerScore:
            print("↳------(Dator vann mest)-------↲")
        elif ingenvann > datorScor and ingenvann > playerScore:
            print("| ingen vann ",ingenvann,"------|")
        else :print("↳-----(Ni har vunnit lika)-----↲")
        e = input("Tryck enter till huvudmeny..")

    elif menyVal == "3":
        print("Program stängs om 3 sekunder...")
        time.sleep(3)
        program = False




    else:
        print("❎Fell input, skriv 1 eller 2 eller 3 ")
        time.sleep(3)
