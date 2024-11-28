from ambiente import ambiente
from agenteSimplesReativo import agenteSimplesReativo as asr
from analiseDesempenho import analiseDesempenho
from agenteBaseadoEmModelo import agenteBaseadoEmModelo as abm
from copy import deepcopy


def main():
    ambienteVar = ambiente(3, 3)
    ambienteVar2 = deepcopy(ambienteVar)
    agente_1 = asr()
    agente_2 = abm()

    desempenho1 = analiseDesempenho(agente_1, ambienteVar)  # Instanciar a análise de desempenho
    desempenho2 = analiseDesempenho(agente_2, ambienteVar2)  # Instanciar a análise de desempenho

    print("Estado inicial do ambiente:")
    #ambienteVar.exibir()

    desempenho1.simular(max_movimentos=1000) 
    print("#----------------------------------#")
    desempenho2.simular(max_movimentos=1000) 



if __name__ == "__main__":
    main()

