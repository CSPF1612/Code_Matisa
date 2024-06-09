from pyModbusTCP.server import DataBank, ModbusServer
import random
from time import sleep


class ServidorMODBUS():
    """
    Classe Servidor Modbus
    """

    def __init__(self, host_ip, port):
        """
        Construtor
        """
        self._db = DataBank()
        self._server = ModbusServer(
            host=host_ip, port=port, no_block=True, data_bank=self._db)

    def run(self):
        """
        Execução do servidor Modbus
        """
        try:
            self._server.start()
            print("Servidor MODBUS em execução")
            while True:
                self._db.set_holding_registers(
                    1000, [random.randrange(int(0.95*400), int(1.05*400))])
                self._db.set_holding_registers(
                    1500, [random.randrange(int(0.95*400), int(1.05*400))])
                print('======================')
                print("Tabela MODBUS")
                print(
                    f'Holding Register \r\n R1000: {self._db.get_holding_registers(1000)} \r\n R2000: {self._db.get_holding_registers(2000)}')
                print(
                    f'Holding Register \r\n R1500: {self._db.get_holding_registers(1500)} \r\n R1501: {self._db.get_holding_registers(1501)}')
                print(
                    f'Holding Register \r\n R1700: {self._db.get_holding_registers(1700)} \r\n R1701: {self._db.get_holding_registers(1701)}')
                print(
                    f'Holding Register \r\n R1702: {self._db.get_holding_registers(1702)} \r\n R1703: {self._db.get_holding_registers(1703)}')
                print(f'Coil \r\n R1000: {self._db.get_coils(1000)}')
                print(f'Coil \r\n R2000: {self._db.get_coils(2000)}')
                sleep(1)
        except Exception as e:
            print("Erro: ", e.args)


s = ServidorMODBUS('localhost', 502)
s.run()
