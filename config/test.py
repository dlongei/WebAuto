from config.logger import Lagger

logger = Lagger(logger="login").get_log()  # 定义日志名字为login,放在测试用例之前
logger.info("test_01:Get url and visit")  # 放在测试用例之中，需要打印日志的地方则调用logger.info

'''
log的基本应用

filename	日志输出到文件的文件名
filemode	文件模式，r[+]、w[+]、a[+]
format	    日志输出的格式
datefat	    日志附带日期时间的格式
style	    格式占位符，默认为 “%” 和 “{}”
level	    设置日志输出级别
stream	    定义输出流，用来初始化 StreamHandler 对象，不能 filename 参数一起使用，否则会ValueError 异常
handles	    定义处理器，用来创建 Handler 对象，不能和 filename 、stream 参数一起使用，否则也会抛出 ValueError 异常
'''

'''
日志级别

OFF	    最高级别，用于关闭日志记录。
FATAL	导致应用程序提前终止的严重错误。
ERROR	其他运行时错误或意外情况。
WARN	使用已过时的API，API的滥用，潜在错误，其他不良的或意外的运行时的状况（但不一定是错误的）。
INFO	重要，输出信息：用来反馈系统的当前状态给最终用户的。
DEBUG	级别最低，可以使用于任何觉得有利于调试时更详细的了解系统运行状态的东东。
TRACE	最详细的信息。一般这些信息只记录到日志文件中。
'''