

def  exibir_menu():print("""
1 - Consultar personagem específico
2 - Consultar artefato específico
3 - Consultar eventos ativos
0 - sair
""")

def analisa_artefato():
    ''

def analisa_eventos():
    ''

def analisa_personagem():
    ''

def main():
    UID_player = int(input('Informe seu UID: '))
    while True:
        exibir_menu()
        option = input('Digite a opção desejada: ') 
        if(option == '1'):
            nome_personagem = input('Digite o nome do personagem desejado: ')
            #lógica para analisá-lo
        elif(option == '2'):
            analisa_artefato()
            #lógica do artefato bolado
        elif(option == '3'):
            analisa_eventos()
            #Pegar as informações dos eventos
        elif(option == '0'):
            break
        else:
            print('Opção inválida, digite 1, 2, 3 ou 0')
            continue
main()
