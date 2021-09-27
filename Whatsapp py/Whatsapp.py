#Import

import pywhatkit

#Codigo 
try: 

    #Mensaje

    pywhatkit.sendwhatmsg ("+571110002233", "Mensaje enviado desde python", 12,40)


    print("Mensaje enviado")

except:

    print ("Mensaje no enviado")



    