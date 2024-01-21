from logger import Logger

# 创建一个Logger对象
log = Logger()

# 使用Logger对象打印不同类型的消息
log.debug('This is a debug message', '1')
log.info('This is an info message')
log.warn('This is a warning message')
log.error('This is an error message')
log.success('This is a success message')