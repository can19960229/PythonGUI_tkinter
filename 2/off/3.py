import jieba
import wordcloud

import imageio


def main():
    mask = imageio.imread("1.png")
    # from scipy.misc import imread
    # mask = imread("1.png")
    f = open("1.txt", "r", encoding="gbk")
    t = f.read()
    print(t)
    f.close()
    ls = jieba.lcut(t)
    txt = " ".join(ls)
    print(txt)
    #   w = wordcloud.WordCloud(font_path="C:\\Windows\\Fonts\\MSYHBD.TTC",\
    #                          mask= mask,width=700, height=700,\
    #                          background_color="white", max_words=50)
    w.generate(txt)
    w.to_file("txt.png")
