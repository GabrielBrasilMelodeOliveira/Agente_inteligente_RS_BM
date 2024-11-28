import random

class agenteBaseadoEmModelo:
    def __init__(self):
        self.posicao = (0, 0)  # Começa no canto superior esquerdo (0, 0)
        self.ultimoLocalVisitado = self.posicao  # Armazenando apenas o último local visitado
    def perceber(self, ambiente):
        return ambiente.obter_estado(self.posicao)

    def agir(self, ambiente):
        percepcao = self.perceber(ambiente)
        if percepcao == "sujo":
            return "sugar"
        else:
            return "mover"

    def mover(self, ambiente):
        x, y = self.posicao

        direcoes = ["cima", "baixo", "esquerda", "direita"]
        opcoesDescartadas = None
        # Descartar a direção se o local já foi visitado (último local visitado)
        if (self.posicao[0] - 1, self.posicao[1]) == self.ultimoLocalVisitado:
            opcoesDescartadas = "cima"
        elif (self.posicao[0] + 1, self.posicao[1]) == self.ultimoLocalVisitado:
            opcoesDescartadas = "baixo"
        elif (self.posicao[0], self.posicao[1] - 1) == self.ultimoLocalVisitado:
            opcoesDescartadas = "esquerda"
        elif (self.posicao[0], self.posicao[1] + 1) == self.ultimoLocalVisitado:
            opcoesDescartadas = "direita"

        # Remover as opções descartadas da lista de direções possíveis
        if opcoesDescartadas:
            direcoes.remove(opcoesDescartadas)
        direcao = random.choice(direcoes)

        self.ultimoLocalVisitado = self.posicao

        # Atualizar a posição com base na direção escolhida
        if direcao == "direita" and y + 1 < ambiente.colunas:
            self.posicao = (x, y + 1)
        elif direcao == "esquerda" and y - 1 >= 0:
            self.posicao = (x, y - 1)
        elif direcao == "baixo" and x + 1 < ambiente.linhas:
            self.posicao = (x + 1, y)
        elif direcao == "cima" and x - 1 >= 0:
            self.posicao = (x - 1, y)
        else:
            #print(f"O agente não pode se mover nessa direção!! {direcao}")
            int = 1
        # Atualizar o último local visitado
        return direcao

    def executar_acao(self, ambiente, acao):
        if acao == "sugar":
            ambiente.alterar_estado(self.posicao, "limpo")  
            #print(f"A célula na posição {self.posicao} foi limpa.")
        elif acao == "mover":
            self.mover(ambiente)
