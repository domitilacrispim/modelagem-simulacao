#Imports------------------------------------------------------------------------------------------#
import math
import modelo_mm1
import numeros_aleatorios as numeros
import estatisticas

#Variaveis----------------------------------------------------------------------------------------#
programa = True
numero_simulacoes = 10
alfa = 0.05

#Funcoes------------------------------------------------------------------------------------------#
while programa:
        resposta = input("simulador: ")
        info = resposta.split(' ')
        resultado = []

        if (resposta == "sair"):
                programa = False
                break
        elif (info[0] == "set_variaveis_globais"):
                #info[1] = Limite da Fila
                #info[2] = Numero de Eventos
                #info[3] = Numero de Simulacoes por Evento
                #info[4] = Valor do Alfa
                modelo_mm1.set_variaveis_globais(info[1], info[2])
                modelo_mm1.print_variaveis_globais()
                numero_simulacoes = int(info[3])
                alfa = float(info[4])

        elif (info[0] == "set_variaveis_chegada"):
                #info[1] = Tipo de Distribuicao (deter, norm, unif, expo)
                #info[2] = Lambda para distribuicao exponencial
                #info[3] = Media para distribuicao normal
                #info[4] = Desvio padrao para distribuicao normal
                #info[5] = Valor inferior para distribuicao uniforme
                #info[6] = Valor superior para distribuicao uniforme
                #info[7] = Valor para tempo deterministico
                modelo_mm1.set_variaveis_chegada(info[1],info[2],info[3],info[4],info[5],info[6],info[7])
                modelo_mm1.print_variaveis_chegada()

        elif (info[0] == "set_variaveis_servico"):
                #info[1] = Tipo de Distribuicao (deter, norm, unif, expo)
                #info[2] = Lambda para distribuicao exponencial
                #info[3] = Media para distribuicao normal
                #info[4] = Desvio padrao para distribuicao normal
                #info[5] = Valor inferior para distribuicao uniforme
                #info[6] = Valor superior para distribuicao uniforme
                #info[7] = Valor para tempo deterministico
                modelo_mm1.set_variaveis_servico(info[1],info[2],info[3],info[4],info[5],info[6],info[7])

                modelo_mm1.print_variaveis_servico()
        elif (info[0] == "set_variaveis_numeros"):
                numeros.set_variaveis(info[1],info[2],info[3],info[4])
                numeros.print_variaveis()

        elif (resposta == "executar"):
                for i in range(numero_simulacoes):
                        print("\nSIMULACAO",i,":----------------------------------------------------------------------------------------")
                        print("")
                        resultado.append(modelo_mm1.simulacao(i))
         #       estatisticas.calculo_simulacoes(resultado, alfa)
        else : 
                print ("-> ERRO: Comando desconhecido\n")
