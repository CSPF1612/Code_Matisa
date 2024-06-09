import socket
import numpy as np
from faces import Face
import threading

class Servidor():
    """
    Classe Servidor - API Socket
    """

    def __init__(self, host, port):
        """
        Construtor da classe servidor
        """
        self._host = host
        self._port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def start(self, modificador=0):
        """
        Método que inicializa a execução do servidor
        """
        endpoint = (self._host, self._port)
        try:
            self.__tcp.bind(endpoint)
            self.__tcp.listen(1)
            print("Servidor iniciado em ", self._host, ": ", self._port)
            while True:
                con, client = self.__tcp.accept()
                # De acordo com o modificador utilizado será escolhido a operação que o cliente ira realizar
                # Caso não tenha sido escolhido um mod>=1 será realizada a operação padrão da calculadora
                if modificador == 1:
                    self._serviceProcessamentoImagens(con, client)
                else:
                    self._serviceCalculadora(con, client)
        except Exception as e:
            print("Erro ao inicializar o servidor", e.args)

    def _serviceCalculadora(self, con, client):
        """
        Método que implementa o serviço de calculadora
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True:
            try:
                msg = con.recv(1024)
                msg_s = str(msg.decode('ascii'))
                resp = eval(msg_s)
                con.send(bytes(str(resp), 'ascii'))
                print(client, " -> requisição atendida")
            except OSError as e:
                print("Erro de conexão ", client, ": ", e.args)
                return
            except Exception as e:
                print("Erro nos dados recebidos pelo cliente ",
                      client, ": ", e.args)
                con.send(bytes("Erro", 'ascii'))
                return

    def _serviceProcessamentoImagens(self, con, client):
        """
        Método que implementa o serviço de calculadora
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True:
            try:
                f = Face()
                
                # Agora o servidor recebera o tamanho da imagem codificada
                img_bytesTam = con.recv(1024)
                # Decodificando o tamanho da imagem para um inteiro
                tam = int.from_bytes(img_bytesTam, 'big')
                
                # Agora o servidor recebera a imagem codificada
                img_bytes = con.recv(tam)
                # A imagem é então modificada pela funcao
                # É retornado a imagem modificada e seu tamaho dps do processo
                img_bytesMod, tamanho_da_imagem_codificado_Mod  = f.facesServidor(img_bytes)
                
                # Agora precisamos enviar o tamanho em bytes da imagem modificada
                con.send(bytes(tamanho_da_imagem_codificado_Mod))
                # Finalmente a imagem modificada é mandada de volta ao cliente
                con.send(bytes(img_bytesMod))
                print(client, " -> requisição atendida")
            except OSError as e:
                print("Erro de conexão ", client, ": ", e.args)
                return
            except Exception as e:
                print("Erro nos dados recebidos pelo cliente ",
                      client, ": ", e.args)
                con.send(bytes("Erro", 'ascii'))
                return

class ServidorMT(Servidor):
    """
    Classe Servidor MultiThread - API Socket
    """
    def __init__(self, host, port):
        """
        Construtor da classe ServidorMT
        """
        super().__init__(host,port)
        self.__threadPool = {}
    
    def start(self, modificador=0):
        """
        Método que inicializa a execução do servidor
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        endpoint = (self._host,self._port)
        try:
            self.__tcp.bind(endpoint)
            self.__tcp.listen(1)
            print("Servidor iniciado em ",self._host,": ", self._port)
            while True:
                con, client = self.__tcp.accept()
                # De acordo com o modificador utilizado será escolhido a operação que o cliente ira realizar
                # Caso não tenha sido escolhido um mod>=1 será realizada a operação padrão da calculadora
                if modificador == 1:
                    self.__threadPool[client] = threading.Thread(target=self._serviceProcessamentoImagens,args=(con,client))
                    self.__threadPool[client].start()
                else:
                    self.__threadPool[client] = threading.Thread(target=self._serviceCalculadora,args=(con,client))
                    self.__threadPool[client].start()
        except Exception as e:
            print("Erro ao inicializar o servidor",e.args)
