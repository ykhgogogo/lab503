import serial

# 创建一个串行端口对象
ser = serial.Serial()

# 构建泵通讯协议的命令字符串
# TODO

# 设置串行端口的参数
try:
    ser = serial.Serial('COM1', 9600)
except serial.SerialException as e:
    print(f"参数设置有误 {e}")
# ser.port = 'COM1'  # 串行端口名称，根据实际情况修改
# ser.baudrate = 9600  # 波特率
# ser.bytesize = serial.EIGHTBITS  # 数据位
# ser.parity = serial.PARITY_NONE  # 校验位
# ser.stopbits = serial.STOPBITS_ONE  # 停止位

# 打开串行端口 同时异常排查
try:
    ser.open()
    print(f"RS232成功打开 和 {ser.port} 建立连接")
except serial.SerialException as e:
    print(f"无法通过RS232打开端口: {e}")

# 字符串匹配命令
while True:
    # 按照提示输入参数
    answer = input('what to do (command(1-16), start_pump(P1, G1, 1换行), stop_pump(P1, G1, 0换行), flow(P1, S3, XXXXX换行), query_pressure(P1, Q2换行), return(), or 设置压力(P1, S6, mmm.nnn换行)) : ') 
    if answer == 'command':
        # TODO
        print('command')
    elif answer == 'start_pump':
        # TODO
        print('start_pump')
    elif answer == 'stop_pump':
        # TODO
        print('stop_pump')
    elif answer == 'flow':
        # TODO
        print('flow')
    elif answer == 'query_pressure':
        # TODO
        print('query_pressure')
    elif answer == 'return':
        # TODO
        print('return')
    elif answer == '设置压力':
        # TODO
        print('设置压力')
    else:
        print('Invalid input. Please try again.')  

# 读取数据
# data = ser.read(10)  # 读取10个字节