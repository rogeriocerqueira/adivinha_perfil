import limpa_tela
import manipular_arquivos

def main():
    print('-------------------------------')
    print('Menu:')
    print('-------------------------------')
    resp = int(input('0 - Introdução \n'
                     '1 - Fazer Perguntas\n'
                     '2 - Cadastrar Perguntas\n'
                     '3 - Sair\n'))
    limpa_tela.limpa_tela()

    if resp ==1:
       manipular_arquivos.buscar_palavra_chaves()

    elif resp == 2:
        manipular_arquivos.cadastrar_perguntas()

    elif resp ==3:
        exit()

    elif resp == 0:
       manipular_arquivos.introducao()

    else:
        print('Opção inválida!')
if __name__ == '__main__':
    main()

