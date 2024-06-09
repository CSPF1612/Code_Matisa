from servidor import ServidorMT

serv = ServidorMT("localhost",9000)
# Para utilizar a funçao de processamento de imagem estabelecer modificador = 1 dentro do start

# De acordo com o modificador utilizado será escolhido a operação que o servidor ira realizar
# A lista de operações possiveis estão no arquivo, na msm pasta, de nome servidor.py
# Caso não tenha sido escolhido um mod>=1 será realizada a operação padrão da calculadora

serv.start(modificador=1)

# Em um ambiente virtual, executar no cmd esse server e deixar rodando
