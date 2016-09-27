import time
import sys

def logBuffer(func):
    type,data = func()
    contentFormat = "{0} [{1}] {2}"
    return contentFormat.format(time.ctime(),type,data)

@logBuffer
def errorLog():
    return "Error","input data error!"

@logBuffer
def warnLog():
    return "Warn","input data Warn"

print(errorLog)
print("-------")
print(warnLog)