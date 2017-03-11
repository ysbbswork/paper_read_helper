import translatetool
import cutpaper
import re
import cutstr
import pdf2txt
import formatforpdf2txt
import easygui


def txtmain(txtfile):
    paralist = cutpaper.cutit(txtfile)
    for each_para in paralist:
        if each_para != '':
            if len(each_para) >= 100:
                littleparalist = cutstr.cut(each_para)  # 这里按句切分一下
                for l in littleparalist:
                    translatetool.translateit(l)
                    # print(l)
            else:
                translatetool.translateit(each_para)
                # print(each_para)


def pdfmain(pdffile, outfile, midfile, formatfile):
    pdftotxtlife = pdf2txt.prase(pdffile, midfile)
    formatforpdf2txt.changethetext(midfile, formatfile)
    with open(formatfile, encoding='utf-8') as f:
        for each_para in f:
            if len(each_para) >= 100:
                littleparalist = cutstr.cut(each_para)  # 这里按句切分一下
                for l in littleparalist:
                    with open(outfile, 'ab') as ff:
                        ff.write(l.encode("utf-8"))
                        ff.write("\n".encode("utf-8"))
                        ff.write(translatetool.translateit(l).encode("utf-8"))
                        ff.write("\n".encode("utf-8"))
            else:
                with open(outfile, 'ab') as ff:
                    ff.write(each_para.encode("utf-8"))
                    ff.write("\n".encode("utf-8"))
                    ff.write(translatetool.translateit(
                        each_para).encode("utf-8"))
                    ff.write("\n".encode("utf-8"))
            # time.sleep(1)


def main():
    easygui.msgbox('请选择你要处理的文件', "欢迎使用ysbbs论文翻译器：ysbbs@qq.com")
    inflie = easygui.fileopenbox(filetypes=["*.pdf", "*.txt"])
    if inflie == None:
        pass
    else:
        infliename = inflie.split("\\")[-1].split(".")[0]
        easygui.msgbox('请选择你要输出到哪里', "欢迎使用ysbbs论文翻译器：ysbbs@qq.com")
        fliesave = easygui.diropenbox("你要保存到哪？", "欢迎使用ysbbs论文翻译器：ysbbs@qq.com")
        if fliesave == None:
            pass
        else:
            outfile = fliesave + "\\" + "%s.txt" % infliename
            midfile = fliesave + "\\" + "%s.data" % infliename
            formatfile = fliesave + "\\" + "%s.format" % infliename
            pdfmain(inflie, outfile, midfile, formatfile)

if __name__ == "__main__":
    main()
