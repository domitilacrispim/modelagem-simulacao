#Imports------------------------------------------------------------------------------------------#
import math
import numpy
from datetime import datetime
from prettytable import PrettyTable

#Variaveis----------------------------------------------------------------------------------------#
iniciar_seed = True
seed = 777
a = 13
b = 66
m = 512

#Funcoes------------------------------------------------------------------------------------------#
def geracao_numero():
        #Variaveis------------------------------#
        global iniciar_seed
        global seed
        global a
        global b
        global m
        #---------------------------------------#

        if (iniciar_seed == True) :
        	seed += datetime.now().microsecond
        	iniciar_seed = False
        seed = ((a * seed + b) % (m - 1))
	
        return (seed + 1)/m

def geracao_distribuicao(variaveis):
        #variaveis[0] = Tipo de Distribuicao (deter, norm, unif, expo)
        #variaveis[1] = Lambda para distribuicao exponencial
        #variaveis[2] = Media para distribuicao normal
        #variaveis[3] = Desvio padrao para distribuicao normal
        #variaveis[4] = Valor inferior para distribuicao uniforme
        #variaveis[5] = Valor superior para distribuicao uniforme
        #variaveis[6] = Valor para tempo deterministico

        #Variaveis------------------------------#
        num1 = geracao_numero()
        num2 = geracao_numero()
        #---------------------------------------#

        if variaveis[0] == "expo":
                return int(math.ceil((-1/variaveis[1])*numpy.log(1-num1)))
        elif variaveis[0] == "norm":
        	aux = math.sqrt((-2*numpy.log(num1)))*math.cos(num2)
        	return int(variaveis[2] + variaveis[3]*aux)
        elif variaveis[0] == "unif":
        	return int(variaveis[4] + (variaveis[5] - variaveis[4])* num1)
		

def geracao_tempo(variaveis):
        #variaveis[0] = Tipo de Distribuicao (deter, norm, unif, expo)
        #variaveis[1] = Lambda para distribuicao exponencial
        #variaveis[2] = Media para distribuicao normal
        #variaveis[3] = Desvio padrao para distribuicao normal
        #variaveis[4] = Valor inferior para distribuicao uniforme
        #variaveis[5] = Valor superior para distribuicao uniforme
        #variaveis[6] = Valor para tempo deterministico
        
        if (variaveis[0] == "deter"):
                return variaveis[6]
        else:
                return geracao_distribuicao(variaveis)

def set_variaveis(v0,v1,v2,v3):
        #Variaveis------------------------------#
        global seed
        global a
        global b
        global m
        #---------------------------------------#

        seed = v0
        a = v1
        b = v2
        m = v3

def print_variaveis():
        tabela1 = PrettyTable(['Seed', 'A', 'B', 'M'])
        tabela1.add_row([seed, a, b, m])
        print (tabela1)
