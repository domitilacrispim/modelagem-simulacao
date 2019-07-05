#Imports------------------------------------------------------------------------------------------#
from numpy import *
from scipy import stats
from prettytable import PrettyTable

#Funcoes------------------------------------------------------------------------------------------#

#Tempo medio de espera na fila
def espera_fila(tempos_espera, tempos_servico1, tempos_servico2 ):
        return sum(tempos_espera)/(len(tempos_servico1)+len(tempos_servico2))

#Probabilidade de um cliente esperar na fila
def probabilidade_fila(tempos_espera,tempos_servico1,tempos_servico2):
        return len(tempos_espera)/(len(tempos_servico1)+len(tempos_servico2))

#Probabilidade do operador ficar livre
def probabilidade_ocioso(tempo_ocioso,tr):
        return tempo_ocioso/tr

#Tempo Medio de Servico
def tempo_servico(tempos_servico):
        if(len(tempos_servico)==0):
                return 0
        return sum(tempos_servico)/len(tempos_servico)

#Tempo Medio Dispendido no Sistema
def tempo_sistema(tempos_espera,tempos_servico1,tempos_servico2):
        return (sum(tempos_espera)+sum(tempos_servico1)+sum(tempos_servico2))/(len(tempos_servico1)+len(tempos_servico2))

#Resultados de uma Simulacao
def resultados(tr, tempos_servico1, tempos_servico2, tempos_espera, tempo_ocioso1, tempo_ocioso2):
        #Variaveis------------------------------#
        ef = espera_fila(tempos_espera, tempos_servico1, tempos_servico2)
        pf = probabilidade_fila(tempos_espera, tempos_servico1, tempos_servico2)
        po= []
        po.append(probabilidade_ocioso(tempo_ocioso1,tr))
        po.append( probabilidade_ocioso(tempo_ocioso2,tr))
        ts = []
        ts.append(tempo_servico(tempos_servico1))
        ts.append(tempo_servico(tempos_servico2))
        t_sistema = tempo_sistema(tempos_espera,tempos_servico1, tempos_servico2 )
        #---------------------------------------#

        return [ef,pf,po,ts,t_sistema]

#Calculo das Estatisticas para Varias Simulacoes
def calculo_simulacoes(matriz_resultados, alfa):
        #Variaveis------------------------------#
        ef = []
        pf = []
        po1 = []
        po2 = []
        ts1 = []
        ts2 = []
        t_sistema = []
        lista_dados = ["espera_fila", "probabilidade_fila", "probabilidade_ocioso1", "probabilidade_ocioso2", "tempo_servico1","tempo_servico2", "tempo_sistema"]
        tabela1 = PrettyTable(['Estatisticas', 'Alfa'])
        tabela2 = PrettyTable(['Dados','Intervalo de Confianca', 'Media', 'Desvio', 'Variancia'])
        #---------------------------------------#

        print("\nESTATISTICAS FINAIS:--------------------------------------------------------------------------------\n")
        tabela1.add_row(['Alfa', "{0:.2f}".format(alfa)])
        print(tabela1)

        for i in matriz_resultados:
                ef.append(i[0])
                pf.append(i[1])
                po1.append(i[2][0])
                po2.append(i[2][1])
                ts1.append(i[3][0])
                ts2.append(i[3][1])
                t_sistema.append(i[4])

        dados = [ef,pf,po1, po2,ts1, ts2,t_sistema]

        for i in range(0,7):
                media = mean(dados[i])
                desvio = std(dados[i])
                variancia = desvio*desvio
                t = stats.t.ppf(1-alfa,len(dados[i]))
                h = t*desvio/sqrt(len(dados[i]))
                tabela2.add_row([lista_dados[i], "["+str("{0:.5f}".format(media-h))+";"+str("{0:.5f}".format(media+h))+"]",
                 "{0:.5f}".format(media), "{0:.5f}".format(desvio), "{0:.5f}".format(variancia)])

        print(tabela2)
        print("")
