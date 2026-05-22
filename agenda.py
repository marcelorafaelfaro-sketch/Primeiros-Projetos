agendinha = []

while True:
    print('''
            Agenda PRO - v0.1
          ESCOLHA SUA OPÇÃO
          0 - SAIR
          1 - NOVO CONTATO
          2 - LISTAR CONTATOS
          3 - ATUALIZAR CONTATOS
          4 - APAGAR CONTATO
''')
    comando_entrada = int(input("Digite o comando: "))
    if comando_entrada == 0:
         print("progrma encerrado")
    elif comando_entrada == 1:
         
