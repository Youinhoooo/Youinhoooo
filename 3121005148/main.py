# -*- coding:utf-8 -*-
from simhash import Simhash
import re
import sys
import argparse

# 读取文本文件
def read_file(files):
    corpus = []
    for file in files:
        with open(file, "r", encoding='UTF-8') as paper:
            corpus.append(paper.read())
    return corpus

# 清除文本文件中的html
def filter_html(html):
    """
    :param html: html
    :return: 返回去掉html的纯净文本
    """
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html).strip()
    return dd


# 求两篇文章相似度
def simhash_similarity(text1, text2):
    """
    :param tex1: 文本1
    :param text2: 文本2
    :return: 返回两篇文章的相似度
    """
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)

    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))

    print(max_hashbit)

    # 汉明距离
    distince = aa_simhash.distance(bb_simhash)
    print(distince)

    similar = 1 - distince / max_hashbit

    return similar

def main_fub(file1,fil2,file3):
    files = []
    files.append(file1)
    files.append(fil2)
    corpus = read_file(files)

    text1 = corpus[0]
    text2 = corpus[1]

    similar = simhash_similarity(text1, text2)
    print("文章相似度： %.2f" % similar)

    f = open(file3, 'w', encoding="utf-8")
    f.write("文章相似度： %.2f" % similar)
    f.close()

if __name__ == '__main__':
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    file_3 = sys.argv[3]

    '''file_1 = r"D:\微信数据\测试文本\orig.txt"
    file_2 = r"D:\微信数据\测试文本\orig_0.8_add.txt"
    file_3 = r"D:\微信数据\测试文本\result.txt"'''

    main_fub(file_1,file_2,file_3)
