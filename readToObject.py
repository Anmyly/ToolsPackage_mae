# 2023/3/27 20:25 Mae
"""
读取文件里的内容
"""
import os
import json


def anyFile_toString(FilePath):
    """"""
    if os.path.exists(FilePath):
        with open(FilePath, "r") as f:
            String = f.read()
        return String
    else:
        raise ValueError("读取的文件不存在！")


def jsonFile_toObject(FilePath):
    """读取json文件，并以python对象输出"""
    if os.path.exists(FilePath):
        # 先确定是不是json文件
        _, suffix = os.path.splitext(os.path.split(FilePath)[1])  # 先分割绝对路径，获取文件名，再分割文件名获取后缀
        if suffix == ".json":
            with open(FilePath, "r") as f:  # open() 获取的文件中的内容都是字符串
                text = f.read()
            if text and text != '""':  # 文档里有内容才能用 json.loads() 方法，即空值不能用 json.loads()
                toObject = json.loads(text)  # 用 json.loads() 方法处理 json的字符串，转变成相应的 python对象
                return toObject
            else:
                raise TypeError("读取的文件，是空文件！")
        else:
            raise TypeError("只能读取 .json 类型 的文件！")
    else:
        raise ValueError("读取的文件不存在")


if __name__ == '__main__':
    file = "ttt.json"
    result = anyFile_toString(file)
    print(result, type(result))

