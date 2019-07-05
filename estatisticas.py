#Imports------------------------------------------------------------------------------------------#
from numpy import *
from scipy import stats
from prettytable import PrettyTable

#Funcoes------------------------------------------------------------------------------------------#

#Tempo medio de espera na fila
def espera_fila(tempos_espera, tempos_servico):
        return sum(tempos_espera)/len(tempos_servico)

#Probabilidade de um cliente esperar na fila
def probabilidade_fila(tempos_espera,tempos_servico):
        return len(tempos_espera)/len(tempos_servico)

#Probabilidade do operador ficar livre
def probabilidade_ocioso(tempo_ocioso,tr):
        return tempo_ocioso/tr

#Tempo Medio de Servico
def tempo_servico(tempos_servico):
        return sum(tempos_servico)/len(tempos_servico)

#Tempo Medio Dispendido no Sistema
def tempo_sistema(tempos_espera,tempos_servico):
        return (sum(tempos_espera)+sum(tempos_servico))/len(tempos_servico)

#Resultados de uma Simulacao
def resultados(tr, tempos_servico, tempos_espera, tempo_ocioso):
        #Variaveis------------------------------#
        ef = espera_fila(tempos_espera, tempos_servico)
        pf = probabilidade_fila(tempos_espera,tempos_servico)
        po = probabilidade_ocioso(tempo_ocioso,tr)
        ts = tempo_servico(tempos_servico)
        t_sistema = tempo_sistema(tempos_espera,tempos_servico)
        #---------------------------------------#

        return [ef,pf,po,ts,t_sistema]

#Calculo das Estatisticas para Varias Simulacoes
def calculo_simulacoes(matriz_resultados, alfa):
        #Variaveis------------------------------#
        ef = []
        pf = []
        po = []
        ts = []
        t_sistema = []
        lista_dados = ["espera_fila", "probabilidade_fila", "probabilidade_ocioso", "tempo_servico", "tempo_sistema"]
        tabela1 = PrettyTable(['Estatisticas', 'Alfa'])
        tabela2 = PrettyTable(['Dados','Intervalo de Confianca', 'Media', 'Desvio', 'Variancia'])
        #---------------------------------------#

        print("\nESTATISTICAS FINAIS:--------------------------------------------------------------------------------\n")
        tabela1.add_row(['Alfa', "{0:.2f}".format(alfa)])
        print(tabela1)

        for i in matriz_resultados:
                ef.append(i[0])
                pf.append(i[1])
                po.append(i[2])
                ts.append(i[3])
                t_sistema.append(i[4])

        dados = [ef,pf,po,ts,t_sistema]

        for i in range(0,5):
                media = mean(dados[i])
                desvio = std(dados[i])
                variancia = desvio*desvio
                t = stats.t.ppf(1-alfa,len(dados[i]))
                h = t*desvio/sqrt(len(dados[i]))
                tabela2.add_row([lista_dados[i], "["+str("{0:.5f}".format(media-h))+";"+str("{0:.5f}".format(media+h))+"]",
                 "{0:.5f}".format(media), "{0:.5f}".format(desvio), "{0:.5f}".format(variancia)])

        print(tabela2)
        print("")
