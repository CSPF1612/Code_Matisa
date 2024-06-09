import cv2
import os
import numpy as np


class Face():
    """
    Classe Face
    """

    def __init__(self):
        """
        Construtor da classe Cliente
        """

    def facesServidor(self, img_bytes):
        # decodificação da imagem
        img = cv2.imdecode(np.frombuffer(
            img_bytes, np.uint8), cv2.IMREAD_COLOR)

        # processamento
        xml_classificador = os.path.join(os.path.relpath(
            cv2.__file__).replace('__init__.py', ''), 'data\haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier(
            xml_classificador)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Desenha retângulos nas áreas onde as faces foram detectadas
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Agora deve enviar a imagem processada de volta ao cliente
        # recodificação para bytes
        _, img_bytesMod = cv2.imencode('.jpg', img)

        # A propria imagem em bytes, deve ser enviado ao cliente!!!
        img_bytesMod = bytes(img_bytesMod)
        # O tamanho da imagem em bytes, deve ser enviado ao servidor!!!
        tamanho_da_imagem_codificado_Mod = len(img_bytesMod).to_bytes(4, 'big')
        
        cv2.imshow('Imagem Processada', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return (img_bytesMod, tamanho_da_imagem_codificado_Mod)

    def facesClienteEnviando(self, caminho_imagem):
        # leitura da imagem
        # Colocar o PATH da imagem a ser enviada para o servidor
        # caminho_imagem = r'E:\CODE_MATISA\UFJF\Inf_Industrial\MEU_python\python3\faces\IMG-20230808-WA0120.jpg'
        img = cv2.imread(caminho_imagem)

        # codificação para bytes
        _, img_bytes = cv2.imencode('.jpg', img)

        # A propria imagem em bytes, deve ser enviado ao servidor!!!
        img_bytes = bytes(img_bytes)
        # O tamanho da imagem em bytes, deve ser enviado ao servidor!!!
        tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
        return (img_bytes, tamanho_da_imagem_codificado)

    def facesClienteRecebendo(self, img_bytesMod):
        # decodificação da imagem
        img = cv2.imdecode(np.frombuffer(
            img_bytesMod, np.uint8), cv2.IMREAD_COLOR)

        cv2.imshow('Imagem Processada', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
