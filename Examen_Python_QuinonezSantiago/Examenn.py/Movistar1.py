import json
def abrirJSON():
    dicFinal={}
    with open("./ Movistar.JSON""r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./ Movistar.JSON""W") as outFile:
        json.dump(dic,outFile)

        Movistar={}

        booleanito = True
        while(booleanito==True):

            print("#######################")
            print("---Hola! Bienvenid@ a Movistar---")
            print("#######################")
            print("¿Que deseas hacer?")
            print("1. Ver nuestros servicios acuales")
            print("2. Ver nuestros planes y servicios")
            print("3. Ver usuaros")
            print("4. Editar usuario")
            print("5. Salir de nuestro menu")
            opt=input(": ")
            ### Leer archivo JSON y pasarlo a dic
            Movistar1=abrirJSON()
            if(opt=="1"):
                print("¿Que deseas hacer?")
                print("1. Ver nuetros servicios actuales")
                opt2=int(input(": "))
                if (opt2==1):
                    print("¿Que deseas ver de nuestros servivios actuales?")
                    print("1. ver uno nuevo")
                    print("2. modificar uno nuevo")
                    print("3. quitar o eliminar uno")
                    print("4. seleccionar uno")
                    opt3=int(input(": "))
                    if(opt3==2):
                        print("####################")
                        print("--Servivios disponibles--")
                        print("#####################")
                        for i in range(len(Movistar1[opt]["Servicioss"])):
                            print(Movistar1[opt]["Servicioss"][i])

                            ## guardar archivo en json
                            guardarJSON(Movistar1)
                            print ("Servicioss")
                            break

            
            






    

