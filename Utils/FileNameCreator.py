import time


def GetFileName():
    resultTime = time.localtime()

    return str(resultTime.tm_year) + "." + str(resultTime.tm_mon) + "." + str(resultTime.tm_mday) + "." + str(
        resultTime.tm_hour) + "." + str(resultTime.tm_min) + "." + str(resultTime.tm_sec)
