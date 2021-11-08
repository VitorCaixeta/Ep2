import random

def cria_pecas():
    dominos = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2],[2,3], [2,4], [2,5], [2,6], [3,3], [3,4], [3,5],[3,6], [4,4], [4,5], [4,6], [5,5], [5,6], [6,6]]
    random.shuffle(dominos)
    return dominos

def inicia_jogo(numerodejogadores,dominos):
    if numerodejogadores == 2:
        x=[dominos[0],dominos[1],dominos[2],dominos[3],dominos[4],dominos[5],dominos[6]]
        y=[dominos[7],dominos[8],dominos[9],dominos[10],dominos[11],dominos[12],dominos[13]]
        z=[dominos[14],dominos[15],dominos[16],dominos[17],dominos[18],dominos[19],dominos[20],dominos[21],dominos[22],dominos[23],dominos[24],dominos[25],dominos[26],dominos[27]]
        jogo = {'jogadores':{0:x,1:y},'monte':z,'mesa':[]}

    if numerodejogadores == 3:
        x=[dominos[0],dominos[1],dominos[2],dominos[3],dominos[4],dominos[5],dominos[6]]
        y=[dominos[7],dominos[8],dominos[9],dominos[10],dominos[11],dominos[12],dominos[13]]
        w=[dominos[14],dominos[15],dominos[16],dominos[17],dominos[18],dominos[19],dominos[20]]
        z=[dominos[21],dominos[22],dominos[23],dominos[24],dominos[25],dominos[26],dominos[27]]
        jogo = {'jogadores':{0:x,1:y,2:w},'monte':z,'mesa':[]}

    if numerodejogadores == 4:
        x=[dominos[0],dominos[1],dominos[2],dominos[3],dominos[4],dominos[5],dominos[6]]
        y=[dominos[7],dominos[8],dominos[9],dominos[10],dominos[11],dominos[12],dominos[13]]
        w=[dominos[14],dominos[15],dominos[16],dominos[17],dominos[18],dominos[19],dominos[20]]
        z=[dominos[21],dominos[22],dominos[23],dominos[24],dominos[25],dominos[26],dominos[27]]
        jogo = {'jogadores':{0:x,1:y,2:w,3:z},'monte':[],'mesa':[]}
    
    return jogo

def verifica_ganhador(dominosnasmaos):
    for jogador, x in dominosnasmaos.items():
        if len(x)==0:
            return jogador
    else:
        return -1
    
def soma_pecas(pecas):
    x=list(map(sum, pecas))
    y= sum(x)
    return y

def posicoes_possiveis(pecasnamao,mesa):
    x=[]
    if len(mesa)==0:
        for i in range(len(pecasnamao)):
            x.append(i)
        return x
    for i in range(len(pecasnamao)):
        if mesa[0][0] in pecasnamao [i] or mesa[-1][-1] in pecasnamao[i]:
            x.append(i)
    return x

def adiciona_na_mesa(domino,mesa):
    if len(mesa)==0:
        mesa.append(domino)
        return domino
    x=[domino[1],domino[0]]
    if domino[0]==mesa[0]:
        mesa.insert(0,x)
    if domino[0]==mesa[0]:
        mesa.insert(0,domino)
    if domino[0]==mesa[-1][-1]:
        mesa.append(domino)
    else:
        mesa.append(x)
    return mesa