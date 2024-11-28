import random

class agenteSimplesReativo:
    def __init__(self):
        self.posicao = (0, 0)  # Começa no canto superior esquerdo (0, 0)
    def perceber(self, ambiente):
        return ambiente.obter_estado(self.posicao)

    def agir(self, ambiente):
        percepcao = self.perceber(ambiente)
        if percepcao == "sujo":
            return "sugar"
        else:
            return "mover"

    def mover(self, ambiente):

        # Direções possíveis
        direcoes = ["cima", "baixo", "esquerda", "direita"]
        
        # Escolher uma direção aleatória
        direcao = random.choice(direcoes)

        x, y = self.posicao
        
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
        return direcao

    def executar_acao(self, ambiente, acao):
        if acao == "sugar":
            ambiente.alterar_estado(self.posicao, "limpo")  # Limpa a célula
            print(f"A célula na posição {self.posicao} foi limpa.")
        elif acao == "mover":
            print(self.mover(ambiente))

