'''
程序分析：使用函数，输出三次 RUNOOB 字符串。
'''
def hello_runoob():
    print ('RUNOOB')
 
def hello_runoobs():
    for i in range(3):
        hello_runoob()
if __name__ == '__main__':
    hello_runoobs()