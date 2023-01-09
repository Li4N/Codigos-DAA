######################################## DYV REG.HOMOGENEAS ######################################################################
def esHomogenea (matriz,iniFilas, finFilas, iniColumnas, finColumnas):
    num = matriz[iniFilas][iniColumnas]
    for i in range (iniFilas,finFilas+1):
        for j in range (iniColumnas, finColumnas+1):
            if (num!=matriz[i][j]):
                return False
    return True
def numRegHomogeneasAux (matriz, iniFilas, finFilas, iniColumnas, finColumnas):
    if (iniFilas==finFilas):
        return 1
    elif esHomogenea (matriz, iniFilas, finFilas, iniColumnas, finColumnas):
        return 1
    else:
        mitadFilas = (iniFilas+finFilas)//2
        mitadColumnas = (iniColumnas+finColumnas) //2

        return numRegHomogeneasAux (matriz, iniFilas, mitadFilas, iniColumnas, mitadColumnas) + \
               numRegHomogeneasAux (matriz, iniFilas, mitadFilas, mitadColumnas+1, finColumnas)+ \
               numRegHomogeneasAux (matriz, mitadFilas+1, finFilas, iniColumnas, mitadColumnas)+ \
               numRegHomogeneasAux (matriz, mitadFilas+1, finFilas, mitadColumnas+1, finColumnas)
def numRegHomogeneas (matriz):
    return numRegHomogeneasAux (matriz, 0, len (matriz)-1, 0, len (matriz[0])-1)

######################################## DYV MERGESORT ######################################################################

def DyVMergeSort (vector, ini, fin):
    if (ini==fin):
        return [vector[ini]]
    else:
        mitad = (ini+fin)//2
        vectorIzqOrdenado=DyVMergeSort(vector, ini, mitad)
        vectorDerOrdenado=DyVMergeSort(vector, mitad+1, fin)
        #Vamos a combinar las dos partes ya ordenadas en un nuevo vector que devolveremos

        nuevo=[]
        i=0
        j=0
        while (i<len (vectorIzqOrdenado)) and (j<len (vectorDerOrdenado)):
            #Vamos a tomar un valor del que sea mas pequeño
            if (vectorIzqOrdenado[i]<vectorDerOrdenado[j]):
                nuevo.append(vectorIzqOrdenado[i])
                i=i+1
            else:
                nuevo.append(vectorDerOrdenado[j])
                j= j + 1
        #Cuando llegamos aquí, una de las dos mitades aun tendrá elementos que hay que pasar a nuevo
        while (i < len(vectorIzqOrdenado)):
            nuevo.append(vectorIzqOrdenado[i])
            i = i + 1
        while (j<len (vectorDerOrdenado)):
            nuevo.append(vectorDerOrdenado[j])
            j = j + 1

        return nuevo
def DyVMergeSort (vector, ini, fin):
    if (ini==fin):
        return [vector[ini]]
    else:
        mitad = (ini+fin)//2
        vectorIzqOrdenado=DyVMergeSort(vector, ini, mitad)
        vectorDerOrdenado=DyVMergeSort(vector, mitad+1, fin)
        #Vamos a combinar las dos partes ya ordenadas en un nuevo vector que devolveremos

        nuevo=[]
        i=0
        j=0
        while (i<len (vectorIzqOrdenado)) and (j<len (vectorDerOrdenado)):
            #Vamos a tomar un valor del que sea mas pequeño
            if (vectorIzqOrdenado[i]<vectorDerOrdenado[j]):
                nuevo.append(vectorIzqOrdenado[i])
                i=i+1
            else:
                nuevo.append(vectorDerOrdenado[j])
                j= j + 1
        #Cuando llegamos aquí, una de las dos mitades aun tendrá elementos que hay que pasar a nuevo
        while (i < len(vectorIzqOrdenado)):
            nuevo.append(vectorIzqOrdenado[i])
            i = i + 1
        while (j<len (vectorDerOrdenado)):
            nuevo.append(vectorDerOrdenado[j])
            j = j + 1

        return nuevo

############################################## DYV MAXIMO Y MINIMO ################################################################
def DyVMaxMin (vector, ini, fin):
    if (ini==fin): #Caso base. Conquista
        return [vector[ini],vector[ini]]
    else:
        mitad = (ini+fin) //2   #Division
        resultado1 = DyVMaxMin (vector, ini, mitad)
        resultado2 = DyVMaxMin (vector, mitad+1, fin)
        #Combinacion
        resultado=[0,0]
        if (resultado1[0]<resultado2[0]):
            resultado[0]=resultado1[0]
        else:
            resultado[0] = resultado2[0]

        if (resultado1[1]>resultado2[1]):
            resultado[1]=resultado1[1]
        else:
            resultado[1] = resultado2[1]
        return resultado

######################################### DYV CIFRASCOMUNES #####################################################################
def ExtraerCifras (numero):
    resultado = [False]*10
    while (numero>0):
        cifra = numero % 10
        numero = numero // 10
        resultado[cifra]=True
    return resultado
def CombinarResultados (resultado1, resultado2):
    resultado = [False] * 10
    for i in range (0,10):
        resultado[i]=resultado1[i] and resultado2[i]
    return resultado
def DyVCifrasComunes (vector, ini, fin):
    if (ini==fin):
        resultado = ExtraerCifras (vector[ini])
        return resultado
    else:
        mitad = (ini+fin) //2
        resultado1 = DyVCifrasComunes (vector, ini,mitad)
        resultado2 = DyVCifrasComunes (vector, mitad+1, fin)
        #Combinacion
        resultado = CombinarResultados (resultado1, resultado2)
        return resultado
vector = [2345,45,1455,514]
resultado = DyVCifrasComunes (vector,0,len (vector)-1)
posUltimoCierto=-1
for i in range (len(resultado)):
    if (resultado[i]):
        posUltimoCierto=i

for i in range (len(resultado)-1):
    if (resultado[i]):
        if (i==posUltimoCierto):
            print (i, end="")
        else:
            print (i, end=" ")
##############################################DYV ELEMENTO MAYORITARIO ################################################################
def DyVMayoritario (vector, ini, fin):
    if (ini==fin):
        return [True, vector[ini]]
    else:
        mitad = (ini + fin) // 2
        [existeMayoritarioMitad1, quienEsMitad1] = DyVMayoritario (vector,ini, mitad)
        [existeMayoritarioMitad2, quienEsMitad2] = DyVMayoritario(vector, mitad+1, fin)

        if (existeMayoritarioMitad1):
            #Si existe mayoritario en la mitad1, puede que sea el mayoritario total de todo el vector
            #Vamos a comprobarlo
            contApariciones=0
            for i in range (ini, fin+1):
                if (vector[i]==quienEsMitad1):
                    contApariciones=contApariciones+1
            if (contApariciones> ((ini+fin+1)//2)):
                return [True, quienEsMitad1]

        if (existeMayoritarioMitad2):
            #Si existe mayoritario en la mitad2, puede que sea el mayoritario total de todo el vector
            #Vamos a comprobarlo
            contApariciones=0
            for i in range (ini, fin+1):
                if (vector[i]==quienEsMitad2):
                    contApariciones=contApariciones+1
            if (contApariciones> ((ini+fin+1)//2)):
                return [True, quienEsMitad2]

        return [False, -1]
######################################### PASAR TODAS CASILLAS LABERINTO (FINDAWAY) #####################################################################
def esFactible(laberinto, N, nueva_x, nueva_y):
    if nueva_x>=0 and nueva_x<N and nueva_y>=0 and nueva_y<N and laberinto[nueva_x][nueva_y]!=1 and laberinto[nueva_x][nueva_y]!=-1:
        return True
    return False

def BTPasarTodas(laberinto, pos_x_actual, pos_y_actual, mov_rel_x, mov_rel_y, N, ceros, pasos):
    exito = False
    intento = 0
    while intento < 4 and not exito:
        nueva_x = pos_x_actual + mov_rel_x[intento]
        nueva_y = pos_y_actual + mov_rel_y[intento]
        # puedo ir a la siguiente pos?
        if esFactible(laberinto, N, nueva_x, nueva_y):
            # si puedes ir, entonces
            valorViejo = laberinto[nueva_x][nueva_y]
            laberinto[nueva_x][nueva_y] = 1
            pasos[0] += 1
            if nueva_x == N-1 and nueva_y == N-1 and pasos[0] == ceros:
                laberinto[nueva_x][nueva_y] = 2
                exito=True
            else:
                exito=BTPasarTodas(laberinto, nueva_x, nueva_y, mov_rel_x, mov_rel_y, N, ceros, pasos)
            if not exito:
                laberinto[nueva_x][nueva_y] = valorViejo
                pasos[0] -= 1
        intento += 1
    return exito

##################################### CUALQUIER SOLUCION ########################################################################
def BT (tablero, pos_x_actual,pos_y_actual, mov_rel_x, mov_rel_y, N):
    exito=False
    intento=0
    while intento<=3 and not exito:
        nueva_x=pos_x_actual+mov_rel_x[intento]
        nueva_y=pos_y_actual+mov_rel_y[intento]
        if nueva_x>=0 and nueva_x<N and nueva_y>=0 and nueva_y<N and tablero[nueva_x][nueva_y]!='X' and tablero[nueva_x][nueva_y]!='M':
            valorViejo=tablero[nueva_x][nueva_y]
            tablero[nueva_x][nueva_y]='X'
            #imprimir (tablero)
            #input ("PULSA ENTER PARA CONTINUAR")
            if (valorViejo=='S'):
                tablero[nueva_x][nueva_y] = 'S'
                exito=True
            else:
                exito=BT(tablero, nueva_x, nueva_y, mov_rel_x, mov_rel_y, N)
            if not exito:
                tablero[nueva_x][nueva_y]=' '
        intento=intento+1
    return exito
########################################### MEJRO SOLUCION ###################################################################   
def esFactible(plano, pos_x_actual, pos_y_actual, mov_rel_x, mov_rel_y, p, nueva_x, nueva_y, n, m, contValor):
    if nueva_x>=0 and nueva_x<n and nueva_y>=0 and nueva_y<m and (plano[nueva_x][nueva_y] == contValor[0] or plano[nueva_x][nueva_y] == 0) : 
            return True
    return False 
# def copiar (origen, destino):
#     for i in range (len (origen)):
#         for j in range (len (origen[i])):
#             destino[i][j]=origen[i][j]
def BTMejorSol(plano, pos_x_actual,pos_y_actual, mov_rel_x, mov_rel_y, p, n, m, contValor, planoMejor, contMejorSol, contActualSol):
    intento = 0
    while intento < 4:
        nueva_x = pos_x_actual + mov_rel_x[intento]
        nueva_y = pos_y_actual + mov_rel_y[intento]
        # puedo ir a la siguiente posición?
        if esFactible(plano, pos_x_actual, pos_y_actual, mov_rel_x, mov_rel_y, p, nueva_x, nueva_y, n, m, contValor):
            # si puedo ir, entonces:
            valorViejo = plano[nueva_x][nueva_y]
            contActualSol[0] += 1
            if (valorViejo == contValor[0]):
                contValor[0] += 1
            plano[nueva_x][nueva_y] = 'R' # valor recogido
            # print("")
            # imprimir(plano)
            # print(contActualSol[0], contMejorSol[0], contValor[0])
            # print("")

            if (valorViejo == p):
                plano[nueva_x][nueva_y] = 'U' # ultimo objeto
                # input("[+] press enter [+]")
                if contActualSol[0] < contMejorSol[0]:
                    # copiar(plano, planoMejor)
                    contMejorSol[0] = contActualSol[0]
            else:
                BTMejorSol(plano, nueva_x,nueva_y, mov_rel_x, mov_rel_y, p, n, m, contValor, planoMejor, contMejorSol, contActualSol)
            
            contActualSol[0] -= 1 
            plano[nueva_x][nueva_y] = valorViejo
            if (valorViejo != 0): # si necesitas buscar un valor exacto, esta cond seria valorViejo == cont[0]-1 (valor anterior)
                contValor[0] -= 1
        intento += 1
############################################# TODAS SOLUCIONES #################################################################
def BTTodasSol (tablero, pos_x_actual,pos_y_actual, mov_rel_x, mov_rel_y, N):
    intento=0
    while intento<=3:
        nueva_x=pos_x_actual+mov_rel_x[intento]
        nueva_y=pos_y_actual+mov_rel_y[intento]
        if nueva_x>=0 and nueva_x<N and nueva_y>=0 and nueva_y<N and tablero[nueva_x][nueva_y]!='X' and tablero[nueva_x][nueva_y]!='M':
            valorViejo=tablero[nueva_x][nueva_y]
            tablero[nueva_x][nueva_y]='X'
            #imprimir (tablero)
            #input ("PULSA ENTER PARA CONTINUAR")
            if (valorViejo=='S'):
                tablero[nueva_x][nueva_y] = 'S'
                imprimir(tablero)
                input ("PULSA ENTER PARA CONTINUAR")
            else:
                BTTodasSol(tablero, nueva_x, nueva_y, mov_rel_x, mov_rel_y, N)
            if (tablero[nueva_x][nueva_y]=='X'):
                tablero[nueva_x][nueva_y]=' '
        intento=intento+1

########################################### MOCHILA BT ###################################################################
import copy

def initData():
    datos = {}
    datos['N'] = 10
    datos['W'] = 1
    datos['Peso'] = [1, 6, 1, 6, 0, 7, 6, 2, 1, 0]
    datos['Valor'] = [7, 0, 2, 7, 3, 5, 4, 4, 6, 5]
    return datos

def initSol(datos):
    sol = {}
    sol['Objetos'] = [0] * datos['N']
    sol['Valor'] = 0
    sol['Peso'] = 0
    return sol

def mejor(sol1, sol2):
    if sol1['Valor'] > sol2['Valor']:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor

def esSolucion(sol, datos):
    return min(datos['Peso']) + sol['Peso'] > datos['W']

def asignar(sol, i, datos):
    sol['Objetos'][i] = 1
    sol['Valor'] += datos['Valor'][i]
    sol['Peso'] += datos['Peso'][i]
    return sol

def borrar(sol, i, datos):
    sol['Objetos'][i] = 0
    sol['Valor'] -= datos['Valor'][i]
    sol['Peso'] -= datos['Peso'][i]
    return sol

def esFactible(sol, i, datos):
    return sol['Peso'] + datos['Peso'][i] <= datos['W']

def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol, datos):
        print("ENCONTRADA: "+str(sol))
        mejorSol = mejor(mejorSol, sol)
    else:
        for i in range(k, datos['N']):
            if esFactible(sol, i, datos):
                sol = asignar(sol, i, datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i+1)
                sol = borrar(sol, i, datos)
    return mejorSol

datos = initData()
sol = initSol(datos)
mejorSol = initSol(datos)
k = 0
print(datos)
print(mejorSol)
print(sol)
mejorSol = mochilaVA(sol, mejorSol, datos, k)
print(mejorSol)
##################################### COLOREADO (DISCORDPIA) #########################################################################
def esFactible(grafo, solucion, etapa, intento):
	for i in range(len(solucion)):
		if grafo[etapa][i] and solucion[i]==intento:
			return False
	return True

def BT(grafo, m, solucion, etapa):
	exito=False
	intento=1
	while intento<=m and not exito:
		if (esFactible(grafo,solucion,etapa,intento)):
			solucion[etapa] = intento
			if (etapa==len(solucion)-1):
				exito=True
			else:
				exito=BT(grafo,m,solucion,etapa+1)
			if not exito:
				solucion[etapa] = 0
		intento += 1
	return exito
##################################### COLOREADO (PROFE) #########################################################################
def initGrafo():
    grafo = {}
    grafo['n'] = 4
    grafo['ady'] = [[1,2,3], [0], [0,3], [0,2]]
    return grafo

def initSol(g):
    return [0] * g['n']

def esSolucion(nodo, grafo):
    return nodo == grafo['n']

def esFactible(grafo, sol, nodo, color):
    factible = True
    i = 0
    adyacencia = grafo['ady'][nodo]
    while factible and i < len(adyacencia):
        if adyacencia[i] < nodo: # sol[adyacencia[i]] != 0
            factible = color != sol[adyacencia[i]]
        i += 1
    return factible
def coloreadoVA(grafo, m, sol, nodo):
    if esSolucion(nodo, grafo):
        esSol = True
    else:
        esSol = False
        color = 1
        while not esSol and color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                esSol, sol = coloreadoVA(grafo, m, sol, nodo+1)
                if not esSol:
                    sol[nodo] = 0
            color += 1
    return esSol, sol
grafo = initGrafo()
m = 4
nodo = 0
sol = initSol(grafo)
esSol, sol = coloreadoVA(grafo, m, sol, nodo)
if esSol:
    print(sol)
else:
    print("No se encuentra solucion")