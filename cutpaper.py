# 把英文文章按段落切割,返回一个list，list的每个元素为一段
import re


def cutit(txtfile):
    p = re.compile('          ')
    line = []
    f = open(txtfile,encoding='utf-8')
    fread = f.read()
    text = re.split(r'\n', fread)
    # for t in text:
    #     print(t)
    f.close()
    return text


# def paracuter(paralist):
#     for each_para in paralist:
#         if len(each_para) >= 100:
#             each_para = re.split(r'.', each_para)


def main():
    print(cutit(r'E:\ysresearch\要看的新论文\fs_backscatter.txt'))

if __name__ == "__main__":
    main()
