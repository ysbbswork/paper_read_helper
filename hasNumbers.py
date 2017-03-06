import re


def hasNumbers(inputString):  # 判断一个字符串是否含有数字
    return bool(re.search(r'\d', inputString))

if hasNumbers('21+') == False:
    print("ok")
else:
    print("not ok")
