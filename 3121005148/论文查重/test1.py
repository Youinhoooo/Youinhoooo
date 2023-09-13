from simhash import Simhash

def simhash_similarity(text1, text2):
    """
    :param tex1: 文本1
    :param text2: 文本2
    :return: 返回两篇文章的相似度
    """
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)

    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))

    # 汉明距离
    distince = aa_simhash.distance(bb_simhash)

    similar = 1 - distince / max_hashbit

    return similar

text1="simhash算法的主要思想是降维，将高维的特征向量映射成一个低维的特征向量，通过两个向量的Hamming Distance来确定文章是否重复或者高度近似。"

text2="simhash算法的主要思想是降维，将高维的特征向量映射成一个低维的特征向量，通过两个向量的Hamming Distance来确定文章是否重复或者高度近似。"

text3 = "simhash算法的主要思想是降维，将高维的特征向量映射成一个低维的特"

text4 = "frsimhatsh算法t的主4要思想是g降5维"

similar=simhash_similarity(text1,text4)
print(similar)
