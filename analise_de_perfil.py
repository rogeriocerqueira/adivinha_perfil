import random
import time
#Abre o arquivo para a leitura e retorna a lista com todas as perguntas do arquivo
def abre_arquivo(nome_arquivo):
    arq_perguntas = []
    try:
        with open(nome_arquivo, 'r') as objeto_arquivo:
            for linha in objeto_arquivo:
                arq_perguntas.append(linha)
            return arq_perguntas
    except IOError:
        print('O arquivo não foi encontrado!')
        exit()

#Limpa a tela no terminal, apenas dando um scroll para cima pois a IDE não limpa nescessáriamente
def limpa_tela(tam = 7):
    clear = '\n'
    print(clear*tam)

''' +----------------------------------------------------------------------------------+
        Através de uma palavra-chave que ajuda a saber qual a pergunta do usuário, 
        o algoritmo compara a pergunta do usuário e responde a pergunta 
    +----------------------------------------------------------------------------------+ '''

def responde_perguntas(lista, nome_arquivo,palavras_chave):

    resp = 'S'
    while resp == 'S' or resp =='s':
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
                if pergunta[j:len(chave)+j] == chave:
                    pergunta = lista[i]
                    pergunta = pergunta[:-1]
                    resposta = seleciona_resposta(i+1, nome_arquivo = 'respostas')
                    meu_perfil[pergunta] = resposta
                    print(meu_perfil)
                    time.sleep(3)
                    limpa_tela()
                    break
             
        if not meu_perfil:
            print('Desculpa essa pergunta, ainda não sabemos responder!')
            time.sleep(3)
            limpa_tela()
                    

        resp = input('Deseja fazer outra pergunta? S/N:')
        limpa_tela()

        if resp == 'N' or resp == 'n':
            main()

        ''' +----------------------------------------------------------------------------------------+
                Agora eu preciso colocar perguntas e respostas numa estrutura de dados pra relacionar
                esses dados. Eu escolhi a Estrutura de Dados dicionário por ser, na minha opinião o
                melhor pra visulizar nessa situação. O próximo passo agora é só relacionar perguntas
                e resposta numa mesma estrutura em arquivos diferentes. Pra isso eu preciso chamar outra
                função que eu criei que vai, ler o arquivo de resposta, pegar uma resposta com base na
                pergunta feita e devolver uma resposta aleartória, que será sorteada a cada chamada da função.
             +---------------------------------------------------------------------------------------+ '''


def main():
    print('-------------------------------')
    print('Menu:')
    print('-------------------------------')
    resp = int(input('0 - Introdução \n1 - Fazer Perguntas \n2 - Inserir Perguntas \n3 - Sair \n'))
    limpa_tela()

    if resp ==1:
        nome_arquivo = input('Digite o nome do arquivo:')
        lista = abre_arquivo(nome_arquivo)

        with open('palavras_chaves', 'r+') as arquivo:
            palavra_chave = []
            for linha in arquivo:
                linha = linha.strip()
                palavra_chave.append(linha)
        responde_perguntas(lista, nome_arquivo, palavra_chave)

    elif resp == 2:

        with open('perguntas', 'a') as arquivo:
            pergunta = input('Digite sua pergunta:')
            if pergunta == '':
                print('Pergunta inválida ou vazia!')
                print('Tente novamente mais tarde!')
                exit()
            else:
                linha = arquivo.write('\n')
                linha = arquivo.write(pergunta)


        with open('respostas', 'a') as arquivo2:
            resp = 'S'
            i = 0
            while resp == 's' or resp == 'S':
                respostas = input('Digite a %d° resposta' %(i+1))
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

        with open('palavras_chaves', 'r+') as arquivo:
            aux =  input('Digite uma palavra chave que tenha haver com a pergunta:')

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

    elif resp ==3:
        exit()

    elif resp == 0:
        with open('welcome', 'r') as arquivo:

            for linha in arquivo:
                linha = linha.strip()
                print(linha)
        print('\n')
        resp = input('Deseja retornar pra o menu anterior S/N ?')
        limpa_tela()
        if resp == 's' or resp =='S':
            if resp =='s' or resp == 's':
                main()
    else:
        print('Opção inválida!')

if __name__ == '__main__':
    main()
