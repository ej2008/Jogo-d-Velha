'''
Jogo da Velha

'''


#definir variavéis
jogadores, tabuleiro, casas, linha = [],[],[],[]
linhas, coluna = 3, ['A','B','C']

#criando as funções
def criar_jogadores():
    return  [['Player 1', 'X', 0, 0], ['Player 2', 'O', 0, 0]]


def criar_tabuleiro(x,y):
    casa = {}
    linha, aux1, aux2 = [], [], []

    for i in range(len(coluna)):
        for j in range(linhas):
            casa[coluna[j] + str(i)]= None
            aux1= coluna[j] + str(i)
            linha.append(casa)
            aux2.append(aux1)
            casa = {}
            aux1 = []

        casas.append(aux2)
        aux2= []
        tabuleiro.append(linha)
        linha = []
    print_tabuleiro(tabuleiro)
    return tabuleiro, casas


def print_tabuleiro(tabuleiro):
    print('Tabuleiro do Joga da Velha\n')
    for i in range(len(tabuleiro)):
        print(tabuleiro[i],'\n')


def check_tabuleiro(p,posicao,tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if posicao in tabuleiro[i][j]:
                if tabuleiro[i][j][posicao] == None:
                    tabuleiro[i][j][posicao]= p
                    print('Casa %s (%i,%s) foi marcada com : %s '%(posicao, i, j, p))
                    return True
                elif tabuleiro[i][j][posicao] != None:
                    print('Está casa já está oucupada, tente outra!\n')
                    return False
    print("Opção inválida, tente novamente! \n")
    return False

#casas [['A0', 'B0', 'C0'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2']]
def check_mate(tabuleiro,casas):
    for i in range(len(tabuleiro)):
        if tabuleiro[i][0][casas[i][0]] == tabuleiro[i][1][casas[i][1]] and\
                tabuleiro[i][1][casas[i][1]] == tabuleiro[i][2][casas[i][2]] or\
                tabuleiro[0][i][casas[0][i]] == tabuleiro[1][i][casas[1][i]] and\
                tabuleiro[1][i][casas[1][i]] == tabuleiro[2][i][casas[2][i]] or \
                tabuleiro[0][0][casas[0][0]] == tabuleiro[1][1][casas[1][1]] and \
                tabuleiro[1][1][casas[1][1]] == tabuleiro[2][2][casas[2][2]] or \
                tabuleiro[2][0][casas[2][0]] == tabuleiro[1][1][casas[1][1]] and \
                tabuleiro[1][1][casas[1][1]] == tabuleiro[2][2][casas[2][2]]:
            print("Check Mate",atual[0])
            return True
    return False


def placar(p1,p2):
    print('Pontuação dos jogadores:')
    if p1[1] == 'X':
        print('%s (%s), com %i jogadas e %i vitórias.' %(p1[0], p1[1], p1[2], p1[3]))
        print('%s (%s), com %i jogadas e %i vitórias.' %(p2[0], p2[1], p2[2], p2[3]))
    else:
        print('%s (%s), com %i jogadas e %i vitórias.' % (p2[0], p2[1], p2[2], p2[3]))
        print('%s (%s), com %i jogadas e %i vitórias.' % (p1[0], p1[1], p1[2], p1[3]))

#Player = Nome, Marca, jogadas, Vitórias
jogadores = criar_jogadores()
atual = jogadores[0]
proximo = jogadores[1]
tabuleiro, casas = criar_tabuleiro(coluna,linhas)

#print(casas)
while True:
    print("Jogada do %s com %s: "%(atual[0], atual[1]))
    posicao = str(input("Digite a posição (A0,...,C2): "))

    if posicao == 'novo':
        print("\n"*3,'Novo Jogo!')
        criar_tabuleiro(coluna,linhas)

    elif posicao == "sair":
        break

    else:
        posicao = posicao.upper()
        if check_tabuleiro(atual[1],posicao,tabuleiro):
            if jogadores[0][2] >= 3 or jogadores[1][2] >= 3:
                if check_mate(tabuleiro, casas):
                    print('Jogador %s venceu o jogo!'%atual[0])
                    atual[3] += 1
                    print('Fim de Jogo!')
            atual[2] = atual[2] + 1
            placar(atual,proximo)
            aux = atual
            atual = proximo
            proximo = aux
            print_tabuleiro(tabuleiro)

