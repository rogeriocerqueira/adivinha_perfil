#Limpa a tela no terminal, apenas dando um scroll para cima pois a IDE não limpa nescessáriamente
def limpa_tela(tam = 7):
    clear = '\n'
    print(clear*tam)