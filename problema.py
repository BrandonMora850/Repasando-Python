piezastornillo = 5
piezastuercas = 3
arandela = 1
tornillos = float(input("Cuantos tornillos desea comprar?: "))
tuercas = float(input("Cuantas tuercas desea comprar? : "))
anrand = float(input("Numero de arandela: "))

if tuercas > tornillos :
    preciofinal= arandela + (tornillos*piezastornillo) + (piezastuercas*tuercas)
    print("La orden esta bien, es un total de : ", preciofinal, "RESUMIDO  tornillos = ",tornillos, " tuercas " ,tuercas)
   
else:
     print("Compurebe orden")
    
