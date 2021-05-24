import time
a = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
     [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
     [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
     [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#a[colonna][riga]

endgame = True
passi = 0
presentation = False
ifgame = False
Rige = 0
Colone = 0
X = 0
Y = 0
Fine = 0

print("*CARICAMENTO E ELABORAZIONE LABIRINTO*")

for R in range (len(a[0])):
     Rige += 1
for C in range(len(a)):
     Colone += 1



for I in range(len(a)):
     if (a[I][0] == 0):
          Y = I
          break

for F in range(len(a)):
     if (a[F][R] == 0):
          Fine = F
          break

print()

print("*CARICAMENTO E ELABORAZIONE LABIRINTO COMPLETATO*\n")

#X = 11
#Y = 6

if (presentation == False):
     print("Benvenuto")
     
     name = input("Come ti chiami? = ")
     
     print("\n"+name + " benvenuto nel labirinto\nAllora " + name + " i comandi per giocare sono:\n" + "per muoversi: W,A,S,D \n" + " W = Sopra\n S = Sotto\n D = Destra\n A = Sinistra\n\n" + "    W  \n  11111\n  00111\nA 10011 D\n  11001\n  11100\n    S  \n")
     
     time.sleep(2)
     
     print("questo gioco per rilevare la posizione attuale del giocatore restuira una 'coordinata' in piano cartesimo con l'origine in alto a sinistra e ricorda che si conta anche lo 0")
     
     time.sleep(2)
     
     startgame = input("Iniziamo? 'Digita Si/No' = ")
     
     if (startgame.lower() == "si"):
          print("bene iniziamo!\n")
          print("Coordinate: " + "Y=" + str(Y) + " X=" + str(X))
          presentation = True
          endgame = False
     
     elif (startgame.lower() == "no"):
          print("Ok, torna quando vorrai giocare")
          presentation = False
          endgame = False
          Rest = input("digita quello che vuoi e premi invio = ")
          print("ciao, ben tornato")
          print("bene iniziamo!")
          print("\nCoordinate: " + "Y=" + str(Y) + " X=" + str(X))
          presentation = True
          endgame = False
          

while endgame == False:
#####################################################################################################################################################################
     if (X == R and Y == Fine):
          print("\nBRAVO",name.upper(),"HAI FINITO IL GIOCO IN",passi,"PASSI")
          presentation == True
          endgame == True
          break
#####################################################################################################################################################################
     posizione = input("\nDigita qua il comando= ")
#####################################################################################################################################################################
     if (posizione.lower() == "w"):#a[colonna][riga]
          if a[Y-1][X] == 1:
               print("\nmuro\n")
               passi += 1

          if a[Y-1][X] == 0:
               print("\npasso fatto\n")
               Y-=1
               passi += 1
#####################################################################################################################################################################
     if (posizione.lower() == "a"):#a[colonna][riga]
          if a[Y][X-1] == 1:
               print("\nmuro\n")
               passi += 1

          if a[Y][X-1] == 0:
               print("\npasso fatto\n")
               X-=1
               passi += 1
#####################################################################################################################################################################
     if posizione.lower() == "s":#a[colonna][riga]
          if (a[Y+1][X] == 1):
               print("\nmuro\n")
               passi += 1

          if a[Y+1][X] == 0:
               print("\npasso fatto\n")
               Y += 1
               passi += 1
#####################################################################################################################################################################
     if posizione.lower() == "d":#a[colonna][riga]
          if a[Y][X+1] == 1:
               print("\nmuro\n")
               passi += 1

          if a[Y][X+1] == 0:
               print("\npasso fatto\n")
               X+=1
               passi += 1
#####################################################################################################################################################################
     print("Coordinate attuali:\n" + "Y=" + str(Y) + " X=" + str(X))
#####################################################################################################################################################################

