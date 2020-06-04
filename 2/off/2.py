

def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '"!@#$%^&*()_+=-':
        txt = txt.replace(ch, " ")
    return txt


def main():
    hamletTxt = getText()
    words = hamletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    # 对一个列表，按照键值对的元素的第二个元素进行排序，由大到小的倒排
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


