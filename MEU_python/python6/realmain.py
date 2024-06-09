from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import kivy
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class MyWidget(BoxLayout):
    def changelb(self, case):
        """
        Método que faz a primeira modificação no visor
        """
        self.first = False
        self.first_change(case)
        """
        Dessa forma, foi feito a primeira digitação
        Agora começa a somar os digitos na tela
        """
        self.building_equation(case)

    def first_change(self, case):
        if self.ids['visor'].text == '0':
            if case == 1:
                self.ids['visor'].text = str(int(self.ids.bt_um.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_um.text))
            elif case == 2:
                self.ids['visor'].text = str(int(self.ids.bt_dois.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_dois.text))
            elif case == 3:
                self.ids['visor'].text = str(int(self.ids.bt_tres.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_tres.text))
            elif case == 4:
                self.ids['visor'].text = str(int(self.ids.bt_quatro.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_quatro.text))
            elif case == 5:
                self.ids['visor'].text = str(int(self.ids.bt_cinco.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_cinco.text))
            elif case == 6:
                self.ids['visor'].text = str(int(self.ids.bt_seis.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_seis.text))
            elif case == 7:
                self.ids['visor'].text = str(int(self.ids.bt_sete.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_sete.text))
            elif case == 8:
                self.ids['visor'].text = str(int(self.ids.bt_oito.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_oito.text))
            elif case == 9:
                self.ids['visor'].text = str(int(self.ids.bt_nove.text))
                self.first = True
                self.last_digit = str(int(self.ids.bt_nove.text))
            elif case == '+':
                self.ids['visor'].text = str(self.ids.bt_mais.text)
                self.first = True
                self.last_digit = str(self.ids.bt_mais.text)
            elif case == '-':
                self.ids['visor'].text = str(self.ids.bt_menos.text)
                self.first = True
                self.last_digit = str(self.ids.bt_menos.text)
            elif case == '.':
                self.ids['visor'].text = str(self.ids.bt_ponto.text)
                self.first = True
                self.last_digit = str(self.ids.bt_ponto.text)

    def building_equation(self, case):
        if self.first:
            ye = 0
        else:
            if case == 1:
                self.ids['visor'].text += str(int(self.ids.bt_um.text))
                self.last_digit = str(int(self.ids.bt_um.text))
            elif case == 2:
                self.ids['visor'].text += str(int(self.ids.bt_dois.text))
                self.last_digit = str(int(self.ids.bt_dois.text))
            elif case == 3:
                self.ids['visor'].text += str(int(self.ids.bt_tres.text))
                self.last_digit = str(int(self.ids.bt_tres.text))
            elif case == 4:
                self.ids['visor'].text += str(int(self.ids.bt_quatro.text))
                self.last_digit = str(int(self.ids.bt_quatro.text))
            elif case == 5:
                self.ids['visor'].text += str(int(self.ids.bt_cinco.text))
                self.last_digit = str(int(self.ids.bt_cinco.text))
            elif case == 6:
                self.ids['visor'].text += str(int(self.ids.bt_seis.text))
                self.last_digit = str(int(self.ids.bt_seis.text))
            elif case == 7:
                self.ids['visor'].text += str(int(self.ids.bt_sete.text))
                self.last_digit = str(int(self.ids.bt_sete.text))
            elif case == 8:
                self.ids['visor'].text += str(int(self.ids.bt_oito.text))
                self.last_digit = str(int(self.ids.bt_oito.text))
            elif case == 9:
                self.ids['visor'].text += str(int(self.ids.bt_nove.text))
                self.last_digit = str(int(self.ids.bt_nove.text))
            elif case == 0:
                self.ids['visor'].text += str(int(self.ids.bt_zero.text))
                self.last_digit = str(int(self.ids.bt_zero.text))
            elif case == '+':
                self.ids['visor'].text += str(self.ids.bt_mais.text)
                self.last_digit = str(self.ids.bt_mais.text)
            elif case == '-':
                self.ids['visor'].text += str(self.ids.bt_menos.text)
                self.last_digit = str(self.ids.bt_menos.text)
            elif case == '.':
                self.ids['visor'].text += str(self.ids.bt_ponto.text)
                self.last_digit = str(self.ids.bt_ponto.text)
            elif case == 'c':
                texto = self.ids['visor'].text
                texto = texto[:-1]
                self.ids['visor'].text = texto
            elif case == 'del':
                self.ids['visor'].text = str(int(self.ids.bt_zero.text))
            elif case == '*':
                if self.last_digit == '+' or self.last_digit == '-' or self.last_digit == '/' or self.last_digit == '*':
                    yo = 1
                else:
                    self.ids['visor'].text += str(self.ids.bt_vezes.text)
                    self.last_digit = str(self.ids.bt_vezes.text)
            elif case == '/':
                if self.last_digit == '+' or self.last_digit == '-' or self.last_digit == '/' or self.last_digit == '*':
                    yo = 1
                else:
                    self.ids['visor'].text += str(self.ids.bt_dividido.text)
                    self.last_digit = str(self.ids.bt_dividido.text)
            elif case == '=':
                self.ids['visor'].text = str(eval(self.ids['visor'].text))
                


class BasicApp(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()


if __name__ == '__main__':
    Window.size = (600, 800)
    Window.fullscreen = False
    BasicApp().run()
