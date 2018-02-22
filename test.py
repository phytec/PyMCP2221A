import PyMCP2221A
import time
gpio = PyMCP2221A.PyMCP2221A()

gpio.Reset()
time.sleep(1)
mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.GPIO_Init()
mcp2221.GPIO_0_OutputMode()
mcp2221.GPIO_1_OutputMode()
mcp2221.GPIO_2_OutputMode()
mcp2221.GPIO_3_OutputMode()

mcp2221.GPIO_0_Output(1)
mcp2221.GPIO_1_Output(1)
mcp2221.GPIO_2_Output(1)
mcp2221.GPIO_3_Output(1)
time.sleep(2)
#mcp2221.ClockOut(mcp2221.CLKDUTY_50,mcp2221.CLKDIV_4)
mcp2221.ADC_1_Init()
mcp2221.ADC_2_Init()
mcp2221.ADC_3_Init()
while 1:
    mcp2221.ADC_DataRead()
    print("----------------")
    print ('AD1: 0x{:02x}'.format(mcp2221.ADC_1_data))
    print ('AD2: 0x{:02x}'.format(mcp2221.ADC_2_data))
    print ('AD3: 0x{:02x}'.format(mcp2221.ADC_3_data))
    time.sleep(2)
