# 把英文文章中不是单词的东西去掉，返回一个只包含4个字母以上的单词的单词列表
import re


def hasNumbers(inputString):  # 判断一个字符串是否含有数字
    return bool(re.search(r'\d', inputString))


def changethetext():
    words = []
    f = open(r'E:\ysresearch\要看的新论文\fs_backscatter.txt')
    for eachline in f:
        t = ['/', ';', '.', '\n', ')', '(', '"', ',', '.']  # 创建标点字符表
        for i in t:
            eachline = eachline.replace(i, ' ')  # 用空格替换标点

        eachline = eachline.split()  # 将空格分割
        for i in eachline:
            if len(i) >= 4 and hasNumbers(i) == False:
                words.append(i)
    f.close()
    return words


def main():
    # wordslist = changethetext()#单个单词翻译，被服务器拒绝
    # for word in wordslist:
    #     translatetool.translateit(word)
    #--------------------------------

    # list1 = cutlist.div_list(wordslist, 20)#调用列表分割后翻译
    # leng = len(list1)
    # for l in range(0, leng):
    #     # print(list1[l])
    #     translatetool.translateit(list1[l])

if __name__ == "__main__":
    main()
