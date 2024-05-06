
import threading
import serial
import serial.tools.list_ports

from pumpi import Pumpi

def main():
    print("Hello World!")
    
    # 获取连接的串口设备情况
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        print("无串口设备。")
    else:
        print("可用的串口设备如下：")
        for comport in ports_list:
            print(list(comport)[0], list(comport)[1])
            
    # 根据 ports_list 的输出结果，连接所有设备
    # 建议设备类型相同，否则需要对每个设备进行不同的处理
    # 注意mac和win的串口形式不同 以COM为例 win是COM开头 mac是/dev/tty开头
    commap = {}
    for port in ports_list:
        if port.device.startswith('COM'):
            ser = serial.Serial(port.device, 9600)
            commap[port.device] = ser
        else:
            # TODO
            print("待定")
            
    while True:
        print("请输入要操作的设备和命令：(例如COM1 P1,G1,1)")
        inputComm = input()
        parts = inputComm.split(" ", 1)
        COMi = parts[0]
        command = parts[1] + "\r\n"
        print(f"COMi: {COMi}, command: {command}")
        try:
            commap[COMi].write(command.encode('utf-8'))
            data = ser.read(10)
            print(f"response: {data}\n")
        except serial.SerialException as e:
            print(f"串口{COMi}写入失败: {e}\n")

if __name__ == '__main__':
    main()