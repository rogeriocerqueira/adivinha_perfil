import random
import time
import limpa_tela
import main

#Mostra na tela uma pequena introducao sobre o programa
def introducao():
    with open('welcome', 'r', encoding="utf-8") as arquivo:

        for linha in arquivo:
            linha = linha.strip()
            print(linha)
    print('\n')
    resp = input('Deseja retornar pra o menu anterior S/N ?')
    limpa_tela.limpa_tela()
    if resp == 's' or resp == 'S':
        main()

""" + ------------------------------------------------------------------------------ +
    Cadastra no arquivo, palavras_chaves, uma palavra chave que vai ser usada como
    chave de busca para responder as perguntas com base no que o usuario perguntou 
    + ------------------------------------------------------------------------------ + """
def cadastrar_palavra_chave():
    with open('palavras_chaves', 'r+', encoding="utf-8") as arquivo:
        aux = input('Digite uma palavra chave que tenha haver com a pergunta:')

        if aux != '':
            linha = arquivo.write('\n')
            linha = arquivo.write(aux)
        else:
            linha = arquivo.write('\n')
            linha = arquivo.write('no key word')

        palavra_chave = []
        for linha in arquivo:
            linha = linha.strip()
            palavra_chave.append(linha)


#Cadastra perguntas no arquivo de perguntas, somente isso
def cadastrar_perguntas():
    with open('perguntas', 'a', encoding="utf-8") as arquivo:
        pergunta = input('Digite a pergunta que voce deseja cadastrar:')
        if pergunta == '':
            print('Pergunta inválida ou vazia!')
            print('Tente novamente mais tarde!')
            exit()
        else:
            linha = arquivo.write('\n')
            linha = arquivo.write(pergunta)

            cadastrar_respostas()
            cadastrar_palavra_chave()


def cadastrar_respostas():
    with open('respostas', 'a', encoding="utf-8") as arquivo2:
        resp = 'S'
        i = 0
        while resp == 's' or resp == 'S':
            respostas = input('Digite a %d° resposta' % (i + 1))
            if i == 0 and respostas != '':

                linha = arquivo2.write('\n')
                linha = arquivo2.write('\n')
                linha = arquivo2.write(respostas)
                i += 1
            elif i > 0 and respostas != '':

                linha = arquivo2.write('\n')
                linha = arquivo2.write(respostas)
                i += 1

            else:
                print('Respostas inválida ou vázia!')

            resp = input('Deseja continuar S/N?')

    print('Respostas cadastradas com sucesso!')


    """
      Aqui eu achei melhor colocar o nome do arquivo como padrão pra não haver
      dúvidas sobre qual arquivo passar, então foi retirado a pergunta pro usuario
      Lembrando que em  lista = abre_arquivo(nome_arquivo), a função abre_arquivos retorna uma 
      lista com todas as perguntas do arquivo
    """
def buscar_palavra_chaves():
    lista = abrir_arquivo('perguntas')
    nome_arquivo = "perguntas"
    with open('palavras_chaves', 'r+') as arquivo:
        palavra_chave = []
        for linha in arquivo:
            linha = linha.strip()
            palavra_chave.append(linha)
    responder_perguntas(lista, nome_arquivo, palavra_chave)

def abrir_arquivo(nome_arquivo):
    arq_perguntas = []
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as objeto_arquivo:
            for linha in objeto_arquivo:
                arq_perguntas.append(linha)
            return arq_perguntas
    except IOError:
        print('O arquivo não foi encontrado!')
        exit()


''' +----------------------------------------------------------------------------------+
        Através de uma palavra-chave que ajuda a saber qual a pergunta do usuário, 
        o algoritmo compara a pergunta do usuário e responde a pergunta 
    +----------------------------------------------------------------------------------+ '''


def responder_perguntas(lista, nome_arquivo, palavras_chave):
    resp = 'S'
    while resp == 'S' or resp == 's':
        pergunta = input('Digite a sua pergunta:')
        meu_perfil = {}
        posicao = 0

        ''' +-------------------------------------------------------------------------------------------+
                O laço abaixo verifica a ocorrência de alguma palavra-chave na string pra saber qual 
                foi a pergunta que o usuário digitou baseado na palavra-chave, caso não seja encontrada 
                nenhuma das palavras-chave, retorna uma reposta negativa para o usuário informando que não
                sabe responder a pergunta! 
            +--------------------------------------------------------------------------------------------+ '''

        for i in range(len(palavras_chave)):
            chave = palavras_chave[i]

            ''' +-----------------------------------------------------------------------------------------+
                        Se a substtring é igual a chave então, pode ser que pergunta é uma pergunta 
                        cadatrada no arquivo (pergunta.txt) ou seja, existe um conjunto de resposta
                        possíveis para ela ser respondida.
                +------------------------------------------------------------------------------------------+ '''

            for j in range(len(pergunta)):
                if pergunta[j:len(chave) + j] == chave:
                    pergunta = lista[i]
                    pergunta = pergunta[:-1]
                    resposta = selecionar_resposta(i + 1, nome_arquivo='respostas')
                    meu_perfil[pergunta] = resposta
                    print(meu_perfil)
                    time.sleep(3)
                    limpa_tela.limpa_tela()
                    break

        if not meu_perfil:
            print('Desculpa essa pergunta, ainda não sabemos responder!')
            time.sleep(3)
            limpa_tela.limpa_tela()

        resp = input('Deseja fazer outra pergunta? S/N:')
        limpa_tela.limpa_tela()

        if resp == 'N' or resp == 'n':
            main.main()

        ''' +----------------------------------------------------------------------------------------+
                Agora eu preciso colocar perguntas e respostas numa estrutura de dados pra relacionar
                esses dados. Eu escolhi a Estrutura de Dados dicionário por ser, na minha opinião o
                melhor pra visulizar nessa situação. O próximo passo agora é só relacionar perguntas
                e resposta numa mesma estrutura em arquivos diferentes. Pra isso eu preciso chamar outra
                função que eu criei que vai, ler o arquivo de resposta, pegar uma resposta com base na
                pergunta feita e devolver uma resposta aleartória, que será sorteada a cada chamada da função.
             +---------------------------------------------------------------------------------------+ '''


def selecionar_resposta(i, nome_arquivo):
    ''' +-------------------------------------------------------------------------------
            Aqui eu tenho que ler o arquivo resposta e com base na posição em que está a
            a pergunta eu sei exatamente qual a string do arquivo repostas eu vou sortear.
            Aqui tenho que garantir 2 coisas, muito importante:

            1°: Que não haja saltos de linhas duplos (ENTER) entre os campos que separam cada
            possível conjunto de repostas, nem mesmo no final do arquivo por que isso vai me permitir que
            linhas em branco serão usadas como identificador de posição do conjunto de respostas que eu devo
            guardar na estrutura (tupla, lista, etc), nesse caso.

            2°: Que o arquivo esteja ordenado. Eu preciso garantir que os arquivo esteja ordenado,
                ou seja, cada espaço em branco no arquivo significa um conjunto de resposta para
                a posssível pergunta feita pelo usuário.

        +-------------------------------------------------------------------------------+'''
    respostas = []
    cont = 0
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if len(linha) == False:
                cont += 1

            elif cont == i and len(linha) > 1:
                respostas.append(linha)
    p = random.choice(respostas)
    return p