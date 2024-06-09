# No python nem todas as funções que podemos utilizar já estão salvas no interpretador original da língua
# Logo, vamos importar algumas bibliotecas, que são listas de funções, para nos ajudar na solução de muitos dos problemas matemáticos e para representação gráfica
# Em alguns casos podemos posicionar um "as" após o nome da biblioteca para facilitar o seu uso durante o código
import control as ct
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import math


class System:
    # Essa função pode receber varios tipos de parametros pra criar a FTMA do sistema, as possibilidades são:
    # num,den -> 2 listas com as constantes que acompanham as potências de 's' do numerador e denominador respectivamente;
    # A,B,C,D -> 4 matrizes do espaço de estados;
    # zeros,polos,Mul -> 2 listas com os zeros e polos da FTMA e o multiplicador;
    #       Ex: [14*(s-4)*(s-5)]/[2*(s-2)*(s-1)] -> zeros=[4,5], polos=[1,2], mul=7
    # FTMA -> a expressão da FTMA usando o 's' da biblioteca 'control', ex:
    #       s=ct.tf('s')
    #       num=s**2+2*s+4
    #       den=s*(s+4)*(s+6)*(s**2+1.4*s+1)
    #       ftma=num/den
    #       sys=System(FTMA=ftma)

    # Por meio dessa função vamos iniciar o código e definir algumas variáveis que serão utilizadas para todas as letras do trabalho
    # self. será o fator que nos permite salvar essas variáveis
    def __init__(self, **kwargs):
        # Para o caso deste trabalho, foi dado todo o desenho do circuito por meio de um diagrama de blocos e com uma legenda sinalizando a composição da planta do sistema G(s)
        # Neste caso podemos obter facilmente a Função Transferência de Malha Aberta:
        # s=ct.tf('s')
        # num=4*(s*s+s+9.25)
        # den=s*(s+4)*(s+1.5)
        # ftma=num/den
        # FTMA=ftma
        # Esta parte do código foi comentada pois estes valores podem ser mudados de forma mais rápida e prática no final deste documento
        # o local onde todas as funções são realmente chamadas para execução

        # Porém, nem sempre temos este caso. Pode ser que tivéssemos obtido as 4 matrizes do Espaço de Estados ou as listas de zeros, polos e o multiplicador
        # Assim, por via das dúvidas, o código tenta todas as opções até que uma delas dê certo:
        try:
            # Obtenção da FTMA e do EE pelas listas de numeradores e denominadores
            self.FTMA = ct.tf(kwargs.get('num'), kwargs.get('den'))
            self.ee = ct.tf2ss(self.FTMA)
        except:
            try:
                # Obtenção do EE e da FTMA pelas 4 matrizes
                self.ee = ct.ss(kwargs.get('A'), kwargs.get(
                    'B'), kwargs.get('C'), kwargs.get('D'))
                self.FTMA = ct.ss2tf(self.ee)
            except:
                try:
                    # # Obtenção da FTMA e do EE pelas listas de zeros, polos e o multiplicador
                    s = ct.tf('s')
                    num = 0
                    den = 0
                    for z in kwargs.get('zeros'):
                        num *= (s+z)
                    for p in kwargs.get('polos'):
                        den *= (s+p)
                    self.FTMA = ct.tf(num, den)*kwargs.get('Mul')
                    self.ee = ct.tf2ss(self.FTMA)
                except:
                    self.FTMA = kwargs.get('FTMA')
                    self.ee = ct.tf2ss(self.FTMA)

        # depois de ter a FTMA(self.FTMA) e o espaço de estados(self.ee), ele calcula os polos, zeros e FTMF
        self.poles = ct.poles(self.FTMA)
        self.zeros = ct.zeros(self.FTMA)
        self.FTMF = ct.feedback(self.FTMA, 1)

    # Daqui pra baixo tem as funções pro trabalho, separando a função requerida para conclusão de cada letra
    # Mas antes devemos definir mais algumas funções para facilitar nosso uso de gráficos de Root Locus
    # Aqui criamos um raio genérico que irá desde a origem do gráfico até os limites da imagem. Se não for definida uma cor, o raio será da cor verde (green = 'g')
    @staticmethod
    def addRay(bound, x, y, color='g'): plt.plot(
        [0, x*bound*5], [0, bound*y*5], color=color)

    # Aqui criamos um círculo genérico cujo centro se posiciona na origem e para um raio que será definido de acordo com nosso problema.
    # Se não for definida uma cor, o raio será da cor vermelha (red = 'r')
    @staticmethod
    def addCircle(axes, radius, color='r'): axes.add_patch(
        plt.Circle((0, 0), radius, color=color, fill=False))

    # Funções necessárias para execução da Letra A
    def letraA(self, supressExtra=False):
        # inicialização de objetos que nos ajudarão ao criar legendas para o gráfico
        figure, axes = plt.subplots()

        # Criaremos 4 listas vazias que futuramente vão conter os valores de x e y de cada polo e zero
        pxs, pys, zxs, zys = [], [], [], []

        # Cálculo do polo desejado
        realDoPoloDesejado = -0.5*1.8
        imagDoPoloDesejado = ((1.8**2)-(realDoPoloDesejado**2))**(1/2)
        # Vamos criar uma nova variável importante que será utilizada pelo resto do programa
        self.poloDesejado = realDoPoloDesejado+(imagDoPoloDesejado*1j)

        # Cálculo dos polos de malha fechada
        polosDeMalhaFechada = ct.poles(self.FTMF)

        # Agora podemos procurar pela lista de polos de MF por aquele que está mais próximo da origem, que será o polo dominante da nossa FTMF
        # Vamos aproveitar a função para adquirir as coordenadas x e y de cada polo e plotá-los com a cor magenta (magenta = 'm')
        poloDominante = polosDeMalhaFechada[0]
        for polo in polosDeMalhaFechada:
            if polo.real > poloDominante.real:
                poloDominante = polo
            pxs.append(polo.real)
            pys.append(polo.imag)
            plt.plot(polo.real, polo.imag, 'x', color='m')

        # Vamos criar uma nova variável importante que será utilizada pelo resto do programa
        self.poloDominante = poloDominante

        # Agora achamos as coordenadas x e y dos zeros e depois dos polos de malha aberta
        for zero in self.zeros:
            zxs.append(zero.real)
            zys.append(zero.imag)
        for polo in self.poles:
            pxs.append(polo.real)
            pys.append(polo.imag)

        # Vamos concatenar as listas de x dos polos e zeros em uma lista com todos os valores de x
        #       faz a mesma coisa para os valores de y
        xs = pxs+zxs
        ys = pys+zys

        # Agora criamos uma lista que contem o menor retangulo que contem todos os zeros e polos, com uma margem de 2
        # Os valores desta lista serão os limites do nosso gráfico de RL
        bounds = [min(xs)-2, max(xs)+2, min(ys)-2, max(ys)+2]

        # Como a linha de amortecimento começa em 0,0 e vai pra cima e pra esquerda, precisamos multiplicar um ponto que está dentro da linha
        #       de amortecimento por um valor grande o suficiente para quando plotar a reta de amortecimento ela não acabe dentro do gráfico
        # A maneira mais prática para adquirir este valor foi analisar os limites da imagem a ser plotada pra esquerda e pra cima e utilizar o maior entre eles
        biggestBound = max(bounds[0], bounds[3])

        # Para plotar os circulos, retas e legenda:
        if supressExtra == False:
            # Plotando as retas de amortecimento e os círculo de raio = Wn, para polo desejado, e o círculo para o polo dominante
            self.addRay(biggestBound, realDoPoloDesejado,
                        imagDoPoloDesejado, color='g')
            self.addRay(biggestBound, realDoPoloDesejado, -
                        imagDoPoloDesejado, color='g')
            self.addCircle(axes, 1.8, color='g')
            self.addRay(biggestBound, poloDominante.real,
                        poloDominante.imag, color='r')
            self.addRay(biggestBound, poloDominante.real, -
                        poloDominante.imag, color='r')
            self.addCircle(axes, np.abs(poloDominante), color='r')
            # Bota as legendas
            PsMF = mpatches.Patch(color='m', label="Polos de Malha Fechada")
            AWPD = mpatches.Patch(
                color='r', label="Amortecimento e wn do polo dominante")
            AWD = mpatches.Patch(
                color='g', label="Amortecimento e wn desejado")
            RL = mpatches.Patch(color='tab:blue', label="Root Locus")
            Zs = mpatches.Patch(color='tab:orange', label="Zeros")
            axes.legend(handles=[PsMF, AWPD, AWD, RL, Zs])
        # Plota o rootLocus
        ct.root_locus(self.FTMA)
        # Configura o plot e chama plt.show()
        plt.grid()
        plt.axis(bounds)
        plt.show()

    # Funções necessárias para execução da Letra B
    def letraB(self):
        figure, axes = plt.subplots()
        # Criamos uma lista de valores que irá de 0 a 50 que será composta por 5001 elementos igualmente espaçados
        # Esta lista serão os valores de amostragem para estudo da resposta ao degrau em função no tempo
        T = np.linspace(0, 50, int(50/0.01)+1)

        # Listas de valores de amplitude (y) para um tempo (t) quando passamos um degrau pelo sistema
        t, y = ct.step_response(self.FTMF, T)
        # Esta parte do código não será utilizada agora, apenas quando chamarmos a função letraB durante a letraE para comparar a resposta ao degrau com e sem os compensadores
        try:
            plt.plot(self.stepResponse[0], self.stepResponse[1])
            old = mpatches.Patch(color='tab:blue', label="Resposta antiga")
            new = mpatches.Patch(color="tab:orange",
                                 label="Resposta compensada")
            axes.legend(handles=[old, new])
        except:
            pass
        # Configura o plot e chama plt.show()
        plt.plot(t, y)
        self.stepResponse = [t, y]
        plt.grid()
        plt.title("Resposta ao degrau")
        plt.show()

    # Para a execução da letraC vamos definir antes uma função para salvar espaço e tempo de execução
    # Esta função será responsável por salvar o maior e segundo maior pico de uma função
    # Isso nos permite o cálculo do período e da frequência aparente do nosso sistema par a resposta ao degrau
    @staticmethod
    def get2Maximums(values):
        diferencaAnterior = 0
        diferencaPosterior = 0
        numberOfMaximumsFound = 0
        index = 1
        maximums = []
        while index < len(values)-1:
            diferencaAnterior = values[index]-values[index-1]
            diferencaPosterior = values[index+1]-values[index]
            if diferencaPosterior < 0 and diferencaAnterior > 0:
                numberOfMaximumsFound += 1
                maximums.append([values[index], index])
                if numberOfMaximumsFound == 2:
                    return maximums
            index += 1

    # Funções necessárias para execução da Letra C
    def letraC(self):
        maximos = self.get2Maximums(self.stepResponse[1])
        print('Sobresinal(valor):', maximos[0][0])
        print('Sobresinal(%):', (((maximos[0][0]-1)/1))*100, "%")
        print('Segundo sobresinal(valor):', maximos[1][0])
        periodo = self.stepResponse[0][maximos[1]
                                       [1]]-self.stepResponse[0][maximos[0][1]]
        print('Período:', periodo)
        print('Frequência:', 1/periodo, "Hz")
        print('wd:', 2*np.pi/periodo, "rad/s")
        print("wd do polo dominante:", self.poloDominante.imag, "rad/s")
        print("Amortecimento do polo dominante:",
              self.poloDominante.real/np.abs(self.poloDominante))

    # Funções necessárias para execução da Letra D
    def letraD(self):
        figure, axes = plt.subplots()
        # Criamos uma lista de valores que irá de 0 a 200 que será composta por 5001 elementos igualmente espaçados
        T = np.linspace(0, 200, int((50/0.01)+1))
        # Para um R(s) = 1/s**2 (rampa), podemos apenas multiplicar nossa FTMF por 1/s para adquirir o C(s) desejado
        # pois o "step_response" já multiplica ela por 1/s

        # Esta parte do código não será utilizada agora, apenas quando chamarmos a função letraD durante a letraE para comparar a resposta à rampa com e sem os compensadores
        try:
            plt.plot(self.rampResponse[0],
                     self.rampResponse[1], color='tab:orange')
            # A resposta a rampa sem os compensadores será desenhada em laranja
            old = mpatches.Patch(color='tab:orange', label="Resposta antiga")
            # A resposta a rampa com os compensadores será desenhada em azul
            new = mpatches.Patch(color="b", label="Resposta compensada")
            # A rampa entrando no sistema será representada em vermelho
            r = mpatches.Patch(color='r', label="Rampa da entrada r(t)")
            axes.legend(handles=[old, new, r])
        except:
            AWPD = mpatches.Patch(
                color='b', label="Comportamento da saída c(t)")
            AWD = mpatches.Patch(color='r', label="Rampa da entrada r(t)")
            axes.legend(handles=[AWPD, AWD])
        t, y = ct.step_response(self.FTMF/ct.tf('s'), T)
        self.rampResponse = [t, y]
        # A saída c(t) sem compensador será representada em azul
        plt.plot(t, y, color='b')
        # A entrada r(t) será representada em vermelho e com uma linha tracejada '----'
        plt.plot(t, t, '--', color='r')
        plt.grid()
        plt.title("Resposta à rampa")
        plt.show()

        # Definindo Kv
        s = ct.tf('s')
        Kv = self.FTMA*s
        zerosKv = ct.zeros(Kv)
        polosKv = ct.poles(Kv)
        # Variável para contar quantos zeros foram removidos
        iz = 0
        # Vamos remover os zeros na origem para facilitar as contas
        i = 0
        while i < len(zerosKv):
            if zerosKv[i].real == 0 and zerosKv[i].imag == 0:
                novoZerosKv = np.delete(zerosKv, i)
                iz = iz+1
            i = i+1
        # Variável para contar quantos pólos foram removidos
        ip = 0
        # Vamos remover os pólos na origem para facilitar as contas
        i = 0
        while i < len(polosKv):
            if polosKv[i].real == 0 and polosKv[i].imag == 0:
                novoPolosKv = np.delete(polosKv, i)
                ip = ip+1
            i = i+1
        # Se Kv possui mais zeros na origem do que pólos, então Kv -> 0
        if iz > ip:
            Kv = 0
        # Se Kv possui mais pólos na origem do que zeros, então Kv -> inf
        if iz < ip:
            Kv = math.inf
        # E se Kv tinha o mesmo número de pólos e zeros na origem, então podemos fazer as contas:
        if iz == ip:
            Kv = abs(np.prod(novoZerosKv)/np.prod(novoPolosKv))
        # Erro de regime permanente
        if Kv == 0:
            Ess = math.inf
        else:
            Ess = 1/Kv
        # Cálculo do erro visto no último ponto do gráfico
        ErroReal = t[int((50/0.01))]-y[int((50/0.01))]
        print('Para um erro de regime permanente Ess = {:.4f} e o erro apresentado no gráfico = {:.4f}:'.format(
            Ess, ErroReal))
        print('Podemos notar que o erro calculado, erro para t -> infinito, é maior que aquele apresentado no último ponto do gráfico, t = 200s.')
        print('Isso nos mostra que, apesar do tempo de simulação ter sido grande, nem sempre podemos tirar conclusões sem fazer os devidos cálculos anteriormente.')

    # Para a execução da letraE vamos definir antes uma função para salvar espaço e tempo de execução
    # Esta função será responsável por salvar o último ponto presente no gráfico onde a resposta ao degrau tem um erro maior ou igual à 5%
    @staticmethod
    def getIndexDoTempoDeAssentamento(stepResponseValues):
        index = len(stepResponseValues)-1
        while index >= 0:
            if stepResponseValues[index] > 1.05 or stepResponseValues[index] < 0.95:
                return index+1
            index -= 1

    # Funções necessárias para execução da Letra E
    def letraE(self):
        # Precisamos criar um compensador de avanço que faz o polo dominante de malha fechada possuir um Wn = 1,8 e Zeta = 0,5
        # Calculamos a deficiencia angular ao pegar 180° e subtrair os ângulos entre os polos de MA e o polo desejado, e adicionar os ângulos entre os zeros e o polo desejado
        deficienciaAngular = 180
        for polo in self.poles:
            deficienciaAngular -= np.angle(self.poloDesejado-polo, True)
        for zero in self.zeros:
            deficienciaAngular += np.angle(self.poloDesejado-zero, True)
        # Para vários valores reais possiveis do zero do compensador de avanço, vamos testar 51 valores igualmente espaçados desde -20 até -0.3
        for x in np.linspace(-20, -0.3, 51):
            # Inicialização de variáveis
            zeroCompensador = x
            # Calcula do angulo entre o zero escolhido e o polo desejado
            zeroAn = (np.angle(self.poloDesejado-zeroCompensador, True))
            # Se esse angulo + (deficiencia angular) for menor que 0, é porque precisamos de mais polos e zeros
            # Mas, como não foi definido se seria possível a utilização de mais de um par de zero e polo, vamos utilizar apenas 1
            if (zeroAn+deficienciaAngular) > 0:
                # Agora calculamos qual deve ser o polo do compensador:
                # x do polo desejado + (y do polo desejado/tan(angulo do polo do compensador)) = -(x do polo do compensador)
                poloCompensador = -(self.poloDesejado.imag/np.tan(
                    (zeroAn+deficienciaAngular)*(2*np.pi/360)))+self.poloDesejado.real
                # Devemos ter certeza que os valores escolhidos para o zero e polo do compensador permitem que gamma > 1, pois gamma = (Polo do compensador) / (Zero do compensador)
                if poloCompensador/zeroCompensador > 1:
                    # Calcula o Gc(s) do compensador de avanço
                    Gc = (ct.tf('s')-zeroCompensador) / \
                        (ct.tf('s')-poloCompensador)
                    # Calcula o Kc necessário para o polo de malha fechada ser o desejado
                    kc = 1/np.abs((self.FTMA*Gc)(self.poloDesejado))

                    # Como queremos reduzir em 10 vezes o erro de regime permanente, devemos aumentar em 10 vezes o Kv
                    # Pois Kv * Ess = 1; então (10*Kv) * (Ess/10) = 1
                    # Logo, temos um novo valor de Kv: Kv' = 10*Kv
                    # Ou, Kv' = Kv * Kc * beta / gamma; onde Kv é o valor já calculado anteriormente de s*G(s) quando s -> 0
                    # Ou seja: beta = 10 * gamma / Kc
                    gamma = poloCompensador/zeroCompensador
                    beta = 10*gamma/kc
                    # Para continuarmos, o beta deve ser maior que 1, assim como gamma
                    if beta > 1:
                        # Agora vamos montar nosso compensador de atraso
                        # Assim como fizemos com o compensador de avanço, vamos testar vários valores para o zero e polo e verificar se estão dentro do permitido
                        for x in np.linspace(-1/5, -1/15, 51):
                            # inicialização de variáveis
                            zeroCompensador = x
                            zeroAn = (
                                np.angle(self.poloDesejado-zeroCompensador, True))
                            # se esse angulo + (deficiencia angular) for menor que 0, é porque precisamos de mais polos e zeros
                            if (zeroAn+(deficienciaAngular)) > 0:
                                poloCompensador = zeroCompensador / beta
                                # Calcula o Gc(s) do compensador de atraso
                                Gc2 = (ct.tf('s')-zeroCompensador) / \
                                    (ct.tf('s')-poloCompensador)
                                # Sua contribuição angular deve ser menor que 5°, e seu módulo entre 0,96 e 1
                                if abs(np.angle(Gc2(self.poloDesejado))) < 5 and 0.96 < abs(Gc2(self.poloDesejado)) <= 1:
                                    T = np.linspace(0, 50, int(50/0.01)+1)
                                    # Agora obtemos nossa nova FTMA, que contem a planta G(s), o compensador de avanço Gc(s), o compensador de atraso Gc2(s), e a constante de ganho Kc
                                    t, y = ct.step_response(
                                        ct.feedback(self.FTMA*Gc*kc*Gc2), T)
                                    sobressinal = self.get2Maximums(y)[0][0]
                                    # Analisamos se nosso sobressinal na resposta ao degrau esta dentro do permitido, desde 1,10 até 1,15
                                    if sobressinal > 1.1 and sobressinal < 1.15:
                                        # Analisamos se o tempo de assentamento em 5% do sinal desejado é menor ou igual à 3,4 segundos
                                        if t[self.getIndexDoTempoDeAssentamento(y)] <= 3.4:
                                            print(
                                                "Tempo de assentamento final:", t[self.getIndexDoTempoDeAssentamento(y)])
                                            # Salvamos a nova FTMA (FTMA velha * Gc(s) * Kc)
                                            self.FTMA *= kc*Gc*Gc2
                                            # Salvamos os novos polos, zeros e FTMF
                                            self.FTMF = ct.feedback(
                                                self.FTMA, 1)
                                            self.zeros = ct.zeros(self.FTMA)
                                            self.poles = ct.poles(self.FTMA)
                                            # Chamamos a letra A e B pra ver a diferença do comportamento do sistema, agora com os equipamentos de controle
                                            self.letraA()
                                            self.letraB()
                                            self.letraC()
                                            self.letraD()
                                            return


# Finalmente vamos chamar para a execução cada uma das letras separadamente
# Podemos redefinir aqui nossa planta G(s) de acordo com a necessidade do problema
s = ct.tf('s')
num = 4*(s*s+s+9.25)
den = s*(s+4)*(s+1.5)
ftma = num/den
sys = System(FTMA=ftma)

sys.letraA()
sys.letraB()
sys.letraC()
sys.letraD()
sys.letraE()
