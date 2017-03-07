import translatetool
import cutpaper
import re
import cutstr

def main():
    txtfile = str(input("please input a txt flie"))
    paralist = cutpaper.cutit(txtfile)
    for each_para in paralist:
        if each_para != '':
            if len(each_para) >= 100:
                littleparalist = cutstr.cut(each_para)#这里分的太粗鲁了
                for l in littleparalist:
                    translatetool.translateit(l)
                    # print(l)
            else:
                translatetool.translateit(each_para)
                # print(each_para)
if __name__ == "__main__":
    main()
