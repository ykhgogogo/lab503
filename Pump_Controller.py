import sys
import serial

# 创建一个串行端口对象
ser = serial.Serial()

# 构建泵通讯协议的命令字符串
# TODO

# 设置串行端口的参数
try:
    ser = serial.Serial('COM1', 9600)
except serial.SerialException as e:
    print(f"参数设置有误 {e}\n")
# ser.port = 'COM1'  # 串行端口名称，根据实际情况修改
# ser.baudrate = 9600  # 波特率
# ser.bytesize = serial.EIGHTBITS  # 数据位
# ser.parity = serial.PARITY_NONE  # 校验位
# ser.stopbits = serial.STOPBITS_ONE  # 停止位

# 打开串行端口 同时异常排查
try:
    ser.open()
    print(f"RS232成功打开 和 {ser.port} 建立连接\n")
except serial.SerialException as e:
    print(f"无法通过RS232打开端口: {e}\n")
    sys.exit(1)

# 字符串匹配命令
while True:
    # 按照提示输入参数
    answer = input('what to do (start_pump(P1,G1,1\n), stop_pump(P1,G1,0\n), flow(P1,S3,XXXXX\n), query_pressure(P1,Q2\n), return(), or set_pressure(P1,S6,mmm.nnn\n)) : ') 
    if answer == 'P1,G1,1\n':
        # TODO
        print('开泵\n')
        data = ser.read(10)  # 读取10个字节
    elif answer == 'P1,G1,0\n':
        # TODO
        print('关泵\n')
        data = ser.read(10)  # 读取10个字节
    elif answer == 'flow':
        # TODO
        print('流量设置\n')
        data = ser.read(10)  # 读取10个字节
    elif answer == 'query_pressure':
        # TODO
        print('压力查询\n')
        data = ser.read(10)  # 读取10个字节
    elif answer == 'return':
        # TODO
        print('返回值\n')
        data = ser.read(10)  # 读取10个字节
    elif answer == '设置压力':
        # TODO
        # 注意泵是否支持压力设设置
        print('压力设置\n')
        data = ser.read(10)  # 读取10个字节
    else:
        print('Invalid input. Please try again.')  

# 读取数据
# data = ser.read(10)  # 读取10个字节