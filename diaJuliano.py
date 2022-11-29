import tkinter as tk


def main():

    window = tk.Tk()
    window.title("Calcular dia Juliano")
    window.geometry("400x300")


    def esBisiesto ():

        anio = entradaAnio.get()
        anio=int(anio)
    
        if not anio % 4 and (anio % 100 or  not anio % 400): 
            return True

    def diasDelMes ():
        
        mes = entradaMes.get()
        mes = int (mes)
        


        if mes == 2:
            
            if esBisiesto ():
                return 29
            else:
                return 28





    def calcularDiaJuliano ():
    
        diaJuliano = 0


        dia = entradaDia.get()
        dia = int(dia)
        mes = entradaMes.get()
        mes = int (mes)
        anio = entradaAnio.get()
        anio = int(anio)

        ene = 31;  mar = 31; abri = 30; may = 31; jun = 30; 
        jul = 31; ago = 31; sep = 30; oct = 31; nov = 30;

        if  diasDelMes() == 29:
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
        anio = str(anio)


        resultado["text"] = "Hoy es el dia " + diaJuliano + " del año " + anio

 





    etiquetaDia = tk.Label(text = "Ingrese el dia actial")
    etiquetaDia.pack()

    entradaDia = tk.Entry()
    entradaDia.pack()

    etiquetaMes = tk.Label(text = "Ingrese el mes actial")
    etiquetaMes.pack()

    entradaMes = tk.Entry()
    entradaMes.pack()

    etiquetaAnio = tk.Label(text = "Ingrese el año actial")
    etiquetaAnio.pack()

    entradaAnio = tk.Entry()
    entradaAnio.pack()

    botonIngresar = tk.Button(text = "Ingresar", command= calcularDiaJuliano)
    botonIngresar.pack()
    
    resultado = tk.Label(text="")
    resultado.pack()

        

    tk.mainloop()
    
if __name__ == "__main__":
    main()

