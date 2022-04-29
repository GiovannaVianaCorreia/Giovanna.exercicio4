primeiroNome = input("Digite seu primeiro nome: ")
dia = input("Dia do nascimento: ")
mes = input("Mes do nascimento: ")
ano = input("Ano do nascimento: ")

primeiraLetra = primeiroNome[0:1].upper()
restanteNome = primeiroNome[1:].lower()

primeiroNome = primeiraLetra + restanteNome


mensagem = "{} nasceu no dia: {}/{}/{}".format(primeiroNome, dia, mes, ano)

print (mensagem)