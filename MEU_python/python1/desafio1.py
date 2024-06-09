dicionario0 = {"Numero do parametro":"","Informacoes":""}

tupla0 = ("Acesso aos Parametros", "0 a 9999", 0, "", "", "", "5-2")
tupla1 = ("Referencia Velocidade", "0 a 65535", "", "", "ro", "READ", "17-1")
tuplax = (tupla0, tupla1)

i = int(input("Qual o numero do parametro: "))

dicionario_blank = {"Descrição":tuplax[i][0], "Faixa de Valores":tuplax[i][1], "Ajuste de Fábrica":tuplax[i][2], "Ajuste do Usuário":tuplax[i][3], "Propriedade":tuplax[i][4], "Grupos":tuplax[i][5], "Página":tuplax[i][6]}

dicionario0["Numero do parametro"] = i
dicionario0["Informacoes"] = dicionario_blank

print(dicionario0)
