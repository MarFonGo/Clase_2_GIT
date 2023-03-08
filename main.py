email=input("Introduzca el email: ")
arroba=False
punto=False
cont=0
extension=[".","c","o","m"]
exten=[]
for i in email:
    if(i=="@"):
        arroba=True
        cont=cont+1
    if arroba:
        if (i=="."):
            punto=True     
    if punto:
        exten.append(i)
if (exten==extension and cont==1):
    print("el email es correcto")
else:
    print("el email es incorrecto")