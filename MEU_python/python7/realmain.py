from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import threading
from pyModbusTCP.client import ModbusClient
from kivy.clock import Clock
from time import sleep
import kivy
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class MyWidget(BoxLayout):
    def connect_server(self):
        """
        Método para conectar o Cliente ao Servidor
        uma vez que a porta e IP de conexão foram fornecidos
        """
        ip = str(self.ids.input_ip.text)
        port = int(self.ids.input_port.text)
        self.c = ClienteMODBUS(ip, port)
        self.read_continuous = False
        self.detect_threading = False
        self.c.start()

    def apply_address(self):
        """
        Método para aplicar o endereço fornecido
        """
        if self.read_continuous == True:
            self.detect_threading = True
            self._ev = Clock.schedule_interval(self.show_output, 1)
        else:
            self.show_output()

    def checkbox_click(self, instance, value):
        if value is True:
            self.read_continuous = True
        else:
            self.read_continuous = False
            if self.detect_threading:
                self._ev.cancel()
            
    def toggle_change(self, case):
        if case == 'coil':
            self.tipo = case
        elif case == 'di':
            self.tipo = case
        elif case == 'ir':
            self.tipo = case
        elif case == 'hr':
            self.tipo = case
            
    def show_output(self, bt=0):
        addr = int(self.ids.input_address.text)
        if self.tipo == 'hr':
            self.value = self.c._cliente.read_holding_registers(addr, 1)[0]
            self.bitcount = '16 bits'
        if self.tipo == 'coil':
            self.value =  self.c._cliente.read_coils(addr, 1)[0]
            self.bitcount = '1 bit'
        if self.tipo == 'ir':
            self.value =  self.c._cliente.read_input_registers(addr, 1)[0]
            self.bitcount = '16 bits'
        if self.tipo == 'di':
            self.value =  self.c._cliente.read_discrete_inputs(addr, 1)[0]
            self.bitcount = '1 bit'
        self.ids['output'].text = str(self.value)
        self.ids['bit_count'].text = str(self.bitcount)

class BasicApp(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()


class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """
    def __init__(self, server_ip, porta, scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip, port=porta)
        self._scan_time = scan_time
    def start(self):
        """
        Método que inicializa a execução do Cliente
        """
        self._cliente.open()

if __name__ == '__main__':
    Window.size = (600, 600)
    Window.fullscreen = False
    BasicApp().run()
