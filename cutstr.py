import re  # 这是一个比较不粗鲁的句子分割函数，以.为分割标志，但是只有句段大于等于10个字符才分


def cut(t):

    m = re.match(r'.', t)
    if m:
        strlist = []
        a = 1
        for e in t:
            # print("e")
            if e == ".":
                # print('if e')
                if a >= 10:
                    # print("a>=")
                    t1 = t[:a]
                    t = t[a:]
                    strlist.append(t1)
                    a = 1
                else:
                    a += 1
            else:
                # print('a+=1')
                a += 1
    else:
        strlist.append(t)
    return strlist
if __name__ == "__main__":
    t = "we look at making backscatter practical for ultra-low power on-body sensors by leveraging radios on ex-isting smartphones and wearables (e.g. WiFi and Bluetooth)."
    print(cut(t))
