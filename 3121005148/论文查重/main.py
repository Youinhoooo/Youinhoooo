from simhash import Simhash
import re
import sys

# 清除文本文件中的html
def filter_html(html):

    dd = re.compile(r'<[^>]+>', re.S).sub('', html).strip()

    return dd

# 读取文本文件
def read_file(files):
    corpus = []
    for file in files:
        with open(file, "r", encoding='UTF-8') as paper:
            corpus.append(filter_html(paper.read()))
    return corpus

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

    #print(max_hashbit)

    # 汉明距离
    distince = aa_simhash.distance(bb_simhash)
    #print(distince)

    similar = 1 - distince / max_hashbit

    return similar

def main_fun(file1,fil2,file3):
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
    

    if len(sys.argv) != 4:
        print('命令行参数个数错误！')
        exit()

    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    file_3 = sys.argv[3]


    main_fun(file_1,file_2,file_3)

