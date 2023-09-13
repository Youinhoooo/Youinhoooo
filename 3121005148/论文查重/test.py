import re
def filter_html(html):
    dd = re.compile(r'<[^>]+>', re.S).sub('', html).strip()
    return dd

file_1 = r"D:\微信数据\测试文本\orig.txt"
file_2 = r"D:\微信数据\测试文本\orig_0.8_dis_15.txt"

files = [file_1,file_2]
for file in files:
    with open(file, "r", encoding='UTF-8') as paper:
        print(filter_html(paper.read()))