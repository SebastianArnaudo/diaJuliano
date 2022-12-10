import tkinter as tk


def main():

    window = tk.Tk()
    window.title("Dia Juliano")
    window.geometry("450x350")

    

   
    def calcularDJ(dia,mes,anio):
        
        anio=anio
        mes=mes
        dia=dia
        
        def esBisiesto (anio):

            anio=int(anio)
    
            if not anio % 4 and (anio % 100 or  not anio % 400): 
                return True

        def diasDelMes (mes,anio):
            
            mes = int (mes)
            


            if mes == 2:
                
                if esBisiesto (anio):
                    return 29
                else:
                    return 28

        def calcularDiaJuliano (dia,mes,anio):
        
                diaJuliano = 0


                
                dia = int(dia)
                

                ene = 31;  mar = 31; abri = 30; may = 31; jun = 30; 
                jul = 31; ago = 31; sep = 30; oct = 31; nov = 30;

                if  diasDelMes(mes,anio) == 29:
                    feb = 29
                else:
                    feb = 28

                
                
                
                

                
                match mes: 
                    case 1: diaJuliano += dia
                    case 2: diaJuliano += ene + dia
                    case 3: diaJuliano += ene + feb + dia
                    case 4: diaJuliano += ene + feb + mar + dia
                    case 5: diaJuliano += ene + feb + mar + abri + dia
                    case 6: diaJuliano += ene + feb + mar + abri + may + dia
                    case 7: diaJuliano += ene + feb + mar + abri + may + jun + dia
                    case 8: diaJuliano += ene + feb + mar + abri + may + jun + jul + dia
                    case 9: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + dia
                    case 10: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + sep + dia
                    case 11: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + sep + oct + dia
                    case 12: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + sep + oct + nov + dia

                diaJuliano = str(diaJuliano)
                

                return diaJuliano

        anio = str(anio)
        mensaje = "Hoy es el dia " + calcularDiaJuliano(dia,mes,anio) + " del año " + anio

        return mensaje

    def diaJuliano():

        string=eFecha.get()
        lista=string.replace("-","/")
        barras=lista.count("/")
        
        if barras==2:
            lista=lista.split("/")
            diaJuliano=calcularDJ(int(lista[0]),int(lista[1]),int(lista[2]))
            salida["text"] = diaJuliano
            salidaError["text"] = ""
            
            try:
                diaJuliano=calcularDJ(int(lista[0]),int(lista[1]),int(lista[2]))
                salida["text"] = diaJuliano
                salidaError["text"] = ""
            except:
                salidaError["text"]="Formato de fecha incorrecto"
                salida["text"]=""
        else:
            salidaError["text"]="Formato de fecha incorrecto"
            salida["text"]=""

    
    lBienvenida= tk.Label(text="Ingrese la fecha actual\n en formato DD/MM/AAA",font=("arial",16))
    lBienvenida.place(x=100,y=10)

    eFecha=tk.Entry(width=20)
    eFecha.place(x= 160, y= 100)

    button = tk.Button(text="Calcular Dia Juliano",bg="green2",command=diaJuliano)
    button.place(x=160,y=200)

    salida=tk.Label(text="",font=("arial",16))
    salida.place(x=70, y=250)

    salidaError=tk.Label(text="",font=("arial",16),fg="Red")
    salidaError.place(x=70, y=300)

    tk.mainloop()
    
if __name__ == "__main__":
    main()