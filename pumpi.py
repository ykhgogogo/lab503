from ast import arg
import serial

# 泵的类定义
class Pumpi:
    def __init__(self, com_port):
        # TODO 参数设置
        self.ser = serial.Serial(com_port, 9600)
        
    def get_command(self, *args):
        command = ','.join(arg) + '\r\n'
        self.ser.write(command.endcode('utf-8'))
        
    def get_response(self):
        data = self.ser.read(10)
        return data