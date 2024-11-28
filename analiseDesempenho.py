class analiseDesempenho:
    def __init__(self, agente, ambiente):
        self.agente = agente
        self.ambiente = ambiente
        self.movimentos = 0  # Contagem de movimentos
        self.movimentosAteLimpar = 0
        self.terminou = False
        self.limpou = 0      # Contagem de células limpas
        self.total_celulas = ambiente.linhas * ambiente.colunas  # Total de células no ambiente
        self.casas_sujas = self.ambiente.contar_sujas()
        self.casas_limpas = self.ambiente.contar_limpas()
        self.casasVisitadas = set()
    

    def registrar_movimento(self):
        self.movimentos += 1  # Incrementa o número de movimentos
        if not self.terminou:
            self.movimentosAteLimpar +=1

    def registrar_limpeza(self, posicao):
        # Verifica se a célula foi limpa e conta a limpeza
        x, y = posicao
        if self.ambiente.grade[x][y] == "limpo":
            self.limpou += 1
        if self.casas_sujas - self.limpou == 0:
            self.terminou = True

    def calcular_eficiencia(self):
        # A eficiência pode ser calculada como a razão entre células limpas e movimentos
        if self.movimentos == 0:
            return 0
        return (self.limpou / self.movimentosAteLimpar) * 100  # Eficiência em %.

    def dificuldade(self):
        dif = (self.casas_sujas / self.total_celulas)*100
        if dif <= 25:
            return "Fácil"
        elif dif <= 50:
            return "Médio"
        elif dif <= 75:
            return "Difícil"
        else:
            return "Extremamente difícil"

    def exibir_desempenho(self):
        # Exibe um relatório simples de desempenho
        print(f"\nRelatório de Desempenho:")
        print(f"Total de casas: {self.total_celulas}")
        print(f"Porcentagem de casas exploradas: {(len(self.casasVisitadas)/self.total_celulas)*100}")
        print(f"Total de casas limpas: {self.casas_limpas}")
        print(f"Total de casas sujas: {self.casas_sujas}")
        print(f"Dificuldade do ambiente: {self.dificuldade()}")
        print(f"Total de movimentos: {self.movimentos}")
        print(f"Total de células limpas pelo agente: {self.limpou}")
        print(f"Total de células sujas restantes: {self.casas_sujas - self.limpou}")
        print(f"Eficiência do agente: {self.calcular_eficiencia():.2f}%")
    

    def simular(self, max_movimentos=10):
        """Simula o comportamento do agente no ambiente e calcula o desempenho"""

        for _ in range(max_movimentos):  # Limitar o número de movimentos
            acao = self.agente.agir(self.ambiente)  # O agente decide a ação
            #print(f"Agente na posição {self.agente.posicao} realizou ação: {acao}")

            if acao == "mover":
                self.agente.mover(self.ambiente)#
                self.registrar_movimento()
                self.casasVisitadas.add(self.agente.posicao)
            elif acao == "sugar":
                x, y = self.agente.posicao
                self.ambiente.alterar_estado((x, y), "limpo")
                self.registrar_limpeza((x, y))

            #self.ambiente.exibir()  # Exibe o ambiente após cada ação

        self.exibir_desempenho()  # Exibe o desempenho após a simulação
