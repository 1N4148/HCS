import sys

# Init

Kesseltemperatur_Ist 	 	= 0
Kesseltemperatur_Soll	 	= 0
Vorlauftemperatur_Ist	 	= 0
Vorlauftemperatur_Soll	 	= 0
Ruecklauftemperatur_Ist  	= 0
Ruecklauftemperatur_Soll 	= 0
Speichertemperatur_Soll		= 0
Speichertemperatur_Ist		= 0

Heizen				= 0

Hysterese_Speicherpumpe		= 2
Hysterese_Mischer		= 2

Mischer_Laufzeit		= 4	# Sekunden pro Kelvin Differenz

f = open("Kessel-Ist","w")

f.write(str(Kesseltemperatur_Ist))
f.write("\n")

f.close()

print(Speichertemperatur_Ist)

# Main loop

while Heizen:

  # Sensoren einlesen
  # LeseEingaenge()
  
  # Paramter einlesen
  # LeseParameter()
  
  # Regeln
  # Steuerung()  

  Raumtemperatur_Abweichung = Raumtemperatur_Soll - Raumtemperatur_Ist

  Vorlauftemperatur_Soll = Raumtemperatur_Abweichung + Heizkurve_Offset + Raumtemperatur_Soll + (Raumtemperatur_Soll - Aussentemperatur_Ist) * Heizkurve_Steigung

  Vorlauftemperatur_Abweichung = Vorlauftemperatur_Soll - Vorlauftemperatur_Ist
  
  if abs(Vorlauftemperatur_Abweichung) > Hysterese_Mischer:
   if Vorlauftemperatur_Abweichung < 0:
    print("Mischer_Zu() Laufzeit:", abs(Vorlauftemperatur_Abweichung * Mischer_Laufzeit))

   elif Vorlauftemperatur_Abweichung > 0:
    print("Mischer_Auf() Laufzeit:", abs(Vorlauftemperatur_Abweichung * Mischer_Laufzeit))
    
  if Speichertemperatur_Ist < Speichertemperatur_Soll:
   Speicher_Laden = 1 
  
  if Kesseltemperatur_Ist > (Speichertemperatur_Ist + Hysterese_Speicherpumpe):
   if Speicher_Laden == 1:
    Speicherpumpe = 1
    
  if Kesseltemperatur_Ist < (Speichertemperatur_Ist - Hysterese_Speicherpumpe):
   Speicherpumpe = 0   
  


  
  print("Hier")
  
  # Parameter schreiben
  # SchreibeParameter() 
  
  # Ausgänge setzen
  # SchreibeAusgaenge()
  
print("Ende")
 