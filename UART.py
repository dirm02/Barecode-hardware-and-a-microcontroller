#Setup UART and print something so we know it's working

#Configurer UART et afficher quelque chose

uart.setup(0, 9600, 8, uart.PARITY_NONE, uart.STOPBITS_1, 0)

print("Scanning")
 
#Set up a couple of variables so they're not nil

#Configurer les variables et les initialisées

data = ""
datac = ""
 
#This function prints out the barcode data and clears all variables so the scanner can read a new barcode. 
#If you wanted to send the data over MQTT, your code would replace the print statement here.

#Cet fonction affichera les codebares et initialisera le scanner pour lire à nouveau.
#Apparament ya un moyen d'envoyé le code a MQTT.
function finish()
    print(datac)
    data = ""
    datac = ""
end
 
#This function concatenates all data received over 150 milliseconds into the variable datac.
#The scanner sends the data in multiple parts to the ESP8266, which needs to be assembled into a single variable.

# Cette fonction attachera le reste des informations reçus aprés 15×10^-2s  vers la variable datac.
#Le scanner envoie l'information en tranche au microcontrolleur ESP8266, qui part la suite doit etre assemblé en un seul variable.

uart.on("data", 0, function(data)
    tmr.alarm(0,150,0,finish)
    datac = datac .. data
end, 0)
