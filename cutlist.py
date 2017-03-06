
# 功能：将list对象分成N个N个的小list


def div_list(ls, n):
    if not isinstance(ls, list) or not isinstance(n, int):
        return []
    ls_len = len(ls)
    if n <= 0 or 0 == ls_len:
        return []
    if n > ls_len:
        return ls
    elif n == ls_len:
        return ls
    else:
        ls_return = []
        for i in range(0, ls_len, n):
            ls_return.append(ls[i:i + n])
        return ls_return

if __name__ == "__main__":
    ls1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(div_list(ls1, 4))
    list1 = div_list(ls1, 4)
    leng = len(list1)
    for l in range(0, leng):
        print(list1[l])
