import socket
from faces import Face

class Cliente():
    """
    Classe Cliente - API Socket
    """

    def __init__(self, server_ip, port):
        """
        Construtor da classe Cliente
        """
        self.__server_ip = server_ip
        self.__port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, modificador=0, caminho_imagem=0):
        """
        Método que inicializa a execução do Cliente
        """
        endpoint = (self.__server_ip, self.__port)
        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso!")
            # De acordo com o modificador utilizado será escolhido a operação que o cliente ira realizar
            # Caso não tenha sido escolhido um mod>=1 será realizada a operação padrão da calculadora
            if modificador == 1:
                self.__methodImageProcessing(caminho_imagem)
            else:
                self.__methodCalculations()
        except:
            print("Servidor não disponível")

    def __methodImageProcessing(self, caminho_imagem):
        """
        Método que implementa as requisições do cliente
        """
        try:
            print(
                f"Caminho da imagem que sera processada: {caminho_imagem}")
            f = Face()
            # Ao executar as operações adquirimos a imagem do path anteriormente determinado
            #codificada em bytes
            # E tambem obtemos o tamanho da imagem codificada
            img_bytes, tamanho_da_imagem_codificado = f.facesClienteEnviando(caminho_imagem)
            
            # Agora mandamos o tamanho da imagem em bytes
            self.__tcp.send(bytes(tamanho_da_imagem_codificado))
            
            # Agora sera mandada a imagem em bytes
            self.__tcp.send(bytes(img_bytes))
            
            # Agora o cliente recebera o tamanho da imagem processada pelo servidor
            img_bytesModTam = self.__tcp.recv(1024)
            # Decodificando o tamanho da imagem para um inteiro
            tam = int.from_bytes(img_bytesModTam, 'big')
            
            # Agora o cliente recebera a imagem processada pelo servidor
            img_bytesMod = self.__tcp.recv(tam)
            
            # Deve-se decodificar a imagem recebida pelo servidor de bytes para um .jpg
            f.facesClienteRecebendo(img_bytesMod)
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)

    def __methodCalculations(self):
        """
        Método que implementa as requisições do cliente
        """
        try:
            msg = ''
            while True:
                msg = input("Digite a operação (x para sair): ")
                if msg == '':
                    continue
                elif msg == 'x':
                    break
                self.__tcp.send(bytes(msg,'ascii'))
                resp = self.__tcp.recv(1024)
                print("= ",resp.decode('ascii'))
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)
