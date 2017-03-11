import re  # 这是一个比较不粗鲁的句子分割函数，以.为分割标志，但是只有句段大于等于10个字符才分n,而且把常用词e.g.等词排除，并不切割[1]开头的引用句


def cut(t):
    m = re.match(r'.', t)
    strlist = []
    badwords = ["e.g.", "i.e.", "A.D.", "h.D."]
    subwords = [".g.", ".e.", ".D.", ".D."]
    if m:
        if not re.match(r'^\[\d+\]?', t):
            a = 1
            for e in t:
                # print("e")
                badword1 = t[a - 2:a + 2]
                badword2 = t[a - 3:a]
                if e == "."and badword1 not in badwords and badword2 not in subwords and not re.match(r'\d\.\d', t[a - 2:a + 1]):
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
    else:
        strlist.append(t)
    return strlist
if __name__ == "__main__":
    t = '''Infrastructur[34]i.e. less  A.D. Backscatter A second class of methods leverages an ambient carrier (e.g. TV or WiFi carrier), and backscatter this signal so that it can be received at a commodity receiver.
    Of these, we do not consider the TV carrier signal used by Ambient Backscatter [34] since its availability is spotty and its signal strength decays a few miles away from a TV tower station.
    So, this technique is less appropriate for continuous monitoring in a mobile scenario. But WiFi Backscatter [30] could be practical since it uses a commodity WiFi transmitter and receiver,'''
    print(cut(t))
