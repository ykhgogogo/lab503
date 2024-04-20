import sys
import time
import serial

# 请务必善于使用log打印错误信息

# 命令和选项的映射
const = {
    # TODO
}

# 创建一个串行端口对象
ser = serial.Serial()

# 设置串行端口的参数
try:
    # 使用之前使用FindCOM.py找到的串口号
    # 根据实际情况修改COM名和波特率
    ser = serial.Serial('COM4', 9600) 
except serial.SerialException as e:
    print(f"参数设置有误 {e}\n")
# ser.port = 'COM1'  # 串行端口名称，根据实际情况修改
# ser.baudrate = 9600  # 波特率
# ser.bytesize = serial.EIGHTBITS  # 数据位
# ser.parity = serial.PARITY_NONE  # 校验位
# ser.stopbits = serial.STOPBITS_ONE  # 停止位

# 打开串行端口 同时异常排查
try:
    print(f"RS232成功打开 和 {ser.port} 建立连接\n")
except serial.SerialException as e:
    print(f"无法通过RS232打开端口: {e}\n")
    sys.exit(1)

# 字符串匹配命令
while True:
    time.sleep(1)
    # 按照提示输入参数
    answer = input('what to do (start_pump(P1,G1,1), stop_pump(P1,G1,0), set_flow(P1,S3,XXXXX), query_pressure(P1,Q2), return(), or set_pressure(P1,S6,mmm.nnn)) : \n') 
    if answer == 'P1,G1,1':
        s = ser.write("P1,G1,1\r\n".encode('utf-8'))
        print(s)
        data = ser.read(10) # 读取10个字节
        print(f'开泵 response: {data}\n') 
        continue 
    elif answer == 'P1,G1,0':
        ser.write('P1,G1,0\r\n'.encode("utf-8"))
        data = ser.read(10)  # 读取10个字节
        print(f'关泵 respnse: {data}\n')
        continue
    elif answer == 'set_flow':
        flow = input('请输入流量值 XX.XXX ml/min: ')
        # TODO 参数校验
        ser.write(f'P1,S3,{flow}\r\n'.encode('utf-8'))
        data = ser.read(10)  # 读取10个字节
        print(f'流量设置 respnse: {data}\n')
        continue
    elif answer == 'query_pressure':
        ser.write('P1,Q2\r\n'.encode('utf-8'))
        data = ser.read(10)  # 读取10个字节
        print(f'压力查询 respnse: {data}\n')
        continue 
    elif answer == 'return':
        # TODO
        print('返回值\n')
        data = ser.read(10)  # 读取10个字节
        continue
    elif answer == '设置压力':
        # TODO
        ser.write('P1,S6,mmm.nnn\r\n'.encode('utf-8'))        
        data = ser.read(10)  # 读取10个字节
        print(f'压力设置 respnse: {data}\n')
        continue
    else:
        print('Invalid input. Please try again.')  

# 读取数据
# data = ser.read(10)  # 读取10个字节