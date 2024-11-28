import random

class ambiente:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.grade = [[random.choice(["sujo", "limpo"]) for _ in range(colunas)] for _ in range(linhas)]
        self.atualizar_casas()

    def exibir(self):
        for linha in self.grade:
            print(" | ".join(linha))
        print("\n")

    def obter_estado(self, posicao):
        x, y = posicao
        return self.grade[x][y]

    def alterar_estado(self, posicao, estado):
        x, y = posicao
        self.grade[x][y] = estado

    def atualizar_casas(self):
        """Atualiza as listas de casas sujas e limpas."""
        self.casasSujas = []
        self.casasLimpas = []

        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.grade[i][j] == "sujo":
                    self.casasSujas.append((i, j))  # Adiciona a posição da casa suja
                else:
                    self.casasLimpas.append((i, j))  # Adiciona a posição da casa limpa


    def contar_sujas(self):
        """Conta quantas casas estão sujas no ambiente."""
        return len(self.casasSujas)

    def contar_limpas(self):
        """Conta quantas casas estão limpas no ambiente."""
        return len(self.casasLimpas)