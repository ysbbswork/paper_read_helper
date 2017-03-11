# 把连字符去掉,把不是句号结尾的句号结尾
import re
import easygui


def hasline(inputString):  # 判断一个字符串是否含有-
    return bool(re.search(r'-\n$', inputString))


def hasdot(inputString):  # 判断一个字符串末尾是否含有./;/,
    return bool(re.search(r'(\.\n$)|(;\n$)|(:\n$)|(,\n$)', inputString))


def changethetext(txtfile, outfile):
    f = open(txtfile, encoding='utf-8')
    for eachline in f:
        if hasline(eachline) == True:
            eachline = eachline.strip('-\n')
        elif hasdot(eachline) == False:
            eachline = eachline.replace('\n', ' ')
            # print("消灭一个")
        with open(outfile, 'ab') as ff:
            ff.write(eachline.encode("utf-8"))
    f.close()
    return


def main():
    easygui.msgbox('请选择你要处理的文件')
    inflie = easygui.fileopenbox()
    infliename = inflie.split("\\")[-1].split(".")[0]
    easygui.msgbox('请选择你要输出到哪里')
    fliesave = easygui.diropenbox("你要保存到哪？")
    outfile = fliesave + "\\" + "%s.txt" % infliename
    midfile = fliesave + "\\" + "%s.data" % infliename
    formatfile = fliesave + "\\" + "%s.format" % infliename
    # changethetext(inflie, outfile,midfile)
if __name__ == "__main__":
    main()
