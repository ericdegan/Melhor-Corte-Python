#Determinar tamanho da chapa
tamanhoChapaL = 2700
tamanhoChapaA = 1800
listaL = []
listaA = []

def medidaInicial():
    global tamanhoChapaL
    global tamanhoChapaA
    respChapa = input('A chapa esta inteira? [S/N] ').upper()
    if respChapa == 'S':
        print('Okay')

    elif respChapa == 'N':
        while True:

            tamanhoChapaL = int(input('Diga a Largura da chapa [max.2700]: '))
            tamanhoChapaA = int(input('Diga Altura da chapa [max.1800]: '))

            if tamanhoChapaL > 2700 or tamanhoChapaA > 1800:
                print('Erro...')
            else:
                break

def listaPecas():
    a = 1
    while True:
        print(f'{a} Peça')
        corteL = int(input('Largura: '))
        corteA = int(input('Altura: '))
        listaL.append(corteL)
        listaA.append(corteA)
        a += 1
        print('Quando nao quiser mais adicionar peças digite [0]')
        if corteA or corteL != 0:
            continue
        else:
            break

medidaInicial()
print('Largura: ',tamanhoChapaL)
print('Altura: ',tamanhoChapaA)


#Colher medidas necessarias
print(f'A primeira chapa tem {tamanhoChapaL} de largura e {tamanhoChapaA} de Altura.')
print('Qual o tamanho das peças que você precisa?')
listaPecas()

print('Parou!')
print(listaA)
print(listaL)


#Fazer os cortes
sobraA = []
sobraL = []
def cortes():
    ChapaA = tamanhoChapaA
    ChapaL = tamanhoChapaL
    a = len(listaL)
    c = 0
    while c != a:
        cortel = listaL[c]
        cortea = listaA[c]
        print(c+1, 'da lista é', cortel)
        c +=1
        ChapaA -= cortea
        ChapaL -= cortel
        if ChapaA < 0 or ChapaL < 0:
            c += 0
            global sobraL
            global sobraA
            sobraA.append(ChapaA + listaA[c-1]) #Encontrar uma forma de reutilizar sobras grandes
            sobraL.append(ChapaL + listaL[c-1]) #Fazer uma função que teste os outros cortes na posição da sobras, e se um desses cortes couber
            ChapaA = 1800                       #Pular o corte da lista de cortes na chapa, antes de seguir.
            ChapaL = 2700
        if ChapaA == 0 or ChapaL == 0:
            c += 0
            ChapaA = 1800
            ChapaL = 2700
cortes()




print('Altura da sobra:', sobraA)
print('Largura da sobra:', sobraL)
#Quantidade de chapas

#Medida das sobras

#Cadastro

#Armazenar medidas em SQL

