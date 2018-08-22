# Barecode-hardware-and-a-microcontroller

> We always considered barcodes to be one of those invisible innovations that profoundly changed the world. What we might recognize as modern barcodes were originally designed as a labor-saving device in the rail and retail industries, but were quickly adopted by factories for automation, hospitals to help prevent medication errors, and a wide variety of other industries to track the movements of goods.

**Bref introduction de la fonctionaliter des codebares electronic, avec leur applications telque: L'automatisation, Les equipements dans les hospitaux et dans d'autre industries pour suivre les mouvements des produits.**

![statbarcod](https://user-images.githubusercontent.com/16779064/44357094-ce5b8280-a476-11e8-8ec8-e3452e80f4a3.PNG)

*Medication errors in hospitals are serious and scary: enter the humble barcode to save lives.
Source: The State and Trends of Barcode, RFID, Biometric and Pharmacy Automation Technologies in US Hospitals*

>The technology is accessible, since all you really need is a printer to make barcodes. If you’re already printing packaging for a product, it only costs you ink, or perhaps a small sticker. Barcodes are so ubiquitous that we’ve ceased noticing them; as an experiment we took a moment to count all of them on our (cluttered) desk – I found 43 and probably didn’t find them all.

**Bla Bla Bla** 

>Despite that, we've only used them in exactly one project: a consultant and friend of mine asked me to build a reference database out of his fairly extensive library. I had a tablet with a camera in 2011, and used it to scan the ISBN barcodes to a list. That list was used to get the information needed to automatically enter the reference to a simple database, all I had to do was quickly verify that it was correct.

# Comment Construire une base de donné de référence pour tracquer tout les "articles,produits,ect.." de votre choix, Avec un systeme codebare sans casser la tirelire!

>Dedicated barcode scanners cost around $20 USD from banggood or DX and are an obvious solution, but that would be boring. I also wanted a more powerful device: a barcode scanner that could directly connect to the Internet so I could track things centrally online without any further hardware. While the idea was hardly unique, it still stuck with me. Recently, I saw a tiny barcode scanner module (Youku E1005) for sale for $17 USD with no datasheet, and I knew the game was on.

**Achete un codebare de 20$ chez :** (https://www.banggood.com) ou **Dans mon site web:** (https://thediscountcomputer.site)

![barcode](https://user-images.githubusercontent.com/16779064/44361056-5abf7280-a482-11e8-885e-a464782f4624.PNG)

>The scanner module itself was very compact, which lent itself well to making a convenient device. It had a generic unlabeled MCU, and a 12-pin ribbon cable connector. It has USB and TTL output as well.

**Le scanneur est compact, il a un MCU general et 12 pin de connection a ribbon**  ![download](https://user-images.githubusercontent.com/16779064/44360898-dd93fd80-a481-11e8-819d-482ce3acab25.jpg) 

**Il a aussi un port pour une sortie USB et TTL** (https://www.sparkfun.com/tutorials/215) (https://en.wikipedia.org/wiki/Terminal_emulator)

# Utilisation et connection:

>Logically, some of the 12 pins were going to be power, ground, USB data lines, and TTL serial output. Typically these modules are used to build hand-held barcode scanners, so also require a trigger to be pressed to activate the scanner. The first step was to desolder the connector so I could get access to the pads underneath.

**Pour connecter l'appareille à un microcontrolleur , on vas simplement enlever la connection ribbon du codebare et souder des files de cuivre**

>The next step was to identify power and ground. Ground was pretty easy since several components were connected to what was clearly a ground plane. The power pin was harder, but there was an IC that looked like a voltage regulator in a SOT-753 package. Given common pinouts, both the enable and the voltage input pins were connected to a single pad.

**Ensuite, on identifie la connection VCC et GND, "ce gars a trouvé le VCC parce qu'il y'a un regulateur de courant qui ressemble a un circuit integré a coté du pin! coup de boule je dirais.  :) "**
> voir image 4 

Having probable inputs for power and ground, I connected 3.3v to the circuit. Nothing happened, which is expected as we've yet to find the trigger pin that activates the device. The easiest thing to do was to quickly connect each remaining pad to ground and see if the trigger was of the ‘active-low’ variety. It turned out it was, and the LED of the device turned on to indicate it was ready to scan.

**Enfin on connect 3.3v au circuit, puis il faut cherché le pin "déclancheur" qui active la machine. Pour cela , essaillé de trouver le pin GND en jouant avec les pin qui reste. Et voilå ! Le LED vas s'allumé comme par magie.** 

![fullanatomie](https://user-images.githubusercontent.com/16779064/44363233-3c10aa00-a489-11e8-8d47-ed3746211b7d.PNG)
> image n°4

# Mesure, Interface et Codage 
>The final step was to find the TTL output. That turned out to be pretty easy now that we could force the device to scan barcodes. We took an arbitrary barcode and scanned it while looking at different pins on my oscilloscope. When we found output, we captured it so we could determine the baud rate later on. The final pinout we found is to the right. The flat cable connector pads were fairly dense, so we soldered wires to components connected to the relevant pads rather than the pads themselves where possible.

**La derniere étape sera de trouver la sortie TTL.Comme le scanneur est fonctionnel,scanne des codebare au pif mais il te faudra un oscilloscope pour mésurer les signals transmis, toujours en jouant avec les 12 pins. Tout en déterminant la vitesse de transmission. Vous remarquerez que le pin ce trouve tout à droite.**

![ref](https://user-images.githubusercontent.com/16779064/44365047-43868200-a48e-11e8-8f49-a8a5b9d62f55.PNG)

>The closest common baudrate is 9600 baud, so that is likely our TTL baudrate. Now, we have all the information we need to connect the barcode scanner module to a microcontroller, in our case an ESP8266 running NodeMCU.

**La vittesse de transmission est de 9600 baud sur la connection ssh (putty), connecter avec le microcontrolleur ESP8266, [voir l'image 5], qui fonctionne avec NodeMCU. Un badA@@ de firmware open source:** (https://github.com/dirm02/nodemcu-firmware)

![oscilloscope](https://user-images.githubusercontent.com/16779064/44365891-9f520a80-a490-11e8-85b3-bed00ef74850.PNG)
>image n°5
 
# Code et Utilisation
>Our code will be very simple: Change the UART speed to 9600 baud, and when any data is received concatenate what comes in for the next 150 milliseconds and print it out. Remember to set the baud rate of your development tool (e.g. ESPlorer) to 9600 as well.

 **Le code sera facile: Changer UART speed to 9600 baud, quand n'importe quelle infomation est reçu, il faut attaché toute autre imformation aprés les 150×10^-3 et affiché le resultat , utilisée l outil de developpement putty , c'est mieux :P**
 

 **Voir le document du code en python**  (https://github.com/dirm02/Tracking-Everything-Everywhere-with-a-barecode-hardware-and-a-microcontroller/blob/master/UART.py)
**You will find the code in python in documentation** (https://github.com/dirm02/Tracking-Everything-Everywhere-with-a-barecode-hardware-and-a-microcontroller/blob/master/UART.py)
 
 # Conclusion
> This worked quite nicely and was able to read various types of barcode without issue. It would be very easy to connect this to a server on the Internet, either directly via MQTT, or using an Internet of Things dashboard. It would even be possible to implement encryption and authentication if you needed.

 **Tout marche a merveille et il y'a moyen de le connecter a une interface IoT(bientot le tut dans mon github). Encore mieux, implementer une encryption(bientot dans mon github)! The sky is the limit :)**
 
 **I am looking for ways to implement this to a java (or C# or C/C++) program of Point-of-sale**
 
 **Je cherche a interconnecté cet application a un programme java (ou C# ou C/C++ )**
 
 # Thank you for reading this and don't forget to shop on my ecommerce : (https://thediscountcomputer.site)
 
 
 
 
 
 
