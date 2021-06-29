
 #Posi => Posicion en el genoma donde comienza el gen. Numero entero.           
 #Posf => Posición en el genoma donde termina el gen. Numero entero
 #cromosoma => Cromosoma donde se situa el gen. Numero entero.
 #variedad => Variedad donde se esta estudiando el gen. Sting (Am, Ch, Gal, Roch, PSA, PSU, TB, TN).
 #reverse => Indica si el alineamiento se ha hecho plus/plus (False) o plus/minus (True). Booleano. 
 #fichero => fichero donde se va a guardar el resultado obtenido. String.

def Busquedagen(posi,posf,cromosoma,variedad,reverse,fichero):    
    fichero= f"c:/Users/alberto/Desktop/bioinfo/TFM/datos/0.fasta-lineas/{variedad}.fa.txt"
    resultado=[]
    cromo=-1 
    conta=0
    for line in open(fichero, 'r'):
        line=line.rstrip()
        if line[0]== ">":
            print(line)
            cromo+=1
            conta=0
        else:
            for i in line:
                conta+=1
                if conta >= posi and conta <= posf and cromo==cromosoma:
                    resultado.append(i)
        if cromo>cromosoma:
            break   
    solucion="".join(resultado)
    if reverse == True:
        solucion=solucion[::-1]
        solucion1=[]
        for nucleotido in solucion:
            if nucleotido == "A":
                solucion1.append("T")
            elif nucleotido == "C":
                solucion1.append("G")
            elif nucleotido == "G":
                solucion1.append("C")
            else:
                solucion1.append("A")
        solucion= "".join(solucion1)    
    file = open(f"C:/Users/alberto/Desktop/bioinfo/sistemas bioinformatcos/bloque 3/TFM/{fichero}.txt", "a")
    file.write(f">{variedad}\r")
    file.write(f"{solucion}\r" )
    file.close()

