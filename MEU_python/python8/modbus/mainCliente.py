from cliente import Cliente

c = Cliente("127.0.0.1", 9000)

# Para utilizar a funçao de processamento de imagem estabelecer modificador = 1
# Digite o path até a imagem a ser processada dentro das aspas simples
# Exemplo: r'PATH'

# MUDAR O PATH DE ACORDO COM PC Q ESTA USANDO
caminho_imagem = r'E:\CODE_MATISA\UFJF\Inf_Industrial\MEU_python\python4\cliente\faces\IMG-20230808-WA0120.jpg'

# De acordo com o modificador utilizado será escolhido a operação que o cliente ira realizar
# A lista de operações possiveis estão no arquivo, na msm pasta, de nome cliente.py
# Caso não tenha sido escolhido um mod>=1 será realizada a operação padrão da calculadora

c.start(modificador=1, caminho_imagem=caminho_imagem)

# Criar novo cmd
# Para executar deve copiar o path da pasta onde esta esse arquivo:
# cd G:\CODE.MATISA\Inf.Ind.Projects\xPROFx\Python\Python 3\Cliente\
# agora escrever "python main.py" para executar o programa
# profit
