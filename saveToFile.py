# 2023/3/27 19:31 Mae
"""
注意：此模块中方法，创建的文件，都是覆盖原先数据的模式。
"""
import os
import json


def to_txt(FilePath, Object):
    """
    FilePath：文件或文件的绝对路径
    Object: 任意类型对象
    """
    Dir, file = os.path.split(FilePath)
    _, suffix = os.path.splitext(file)
    # 先保证 有文件后缀，且后缀为 .txt
    if suffix and suffix != ".txt":
        raise TypeError("文件不是txt文件类型，请输入正确的以 .txt 为后缀的文件！")
    # 再保证目录存在，不存则就创建
    if Dir and not os.path.exists(Dir):  # 路径中的目录不为空，且不存在 的情况
        try:
            os.makedirs(Dir)  # 创建目录
        except OSError:
            raise TypeError("你输入的目录不正确！请输入文件的绝对路径，或者相对路径！相对路径是类似./dir/file的格式！")
    # 最后创建文件
    with open(FilePath, "w", encoding="utf-8") as file:
        file.write(Object)


def to_json(FilePath, Object, ensure_ascii=False):
    """
    - # 把 python对象（字典 或 列表 对象；或者是 字典 或 列表 格式的字符串（内部转成python对象）），存到json文件中
    - ## FilePath：文件或文件的绝对路径
    - ## Object: python的 字典 或 列表 对象；或者是 字典 或 列表 格式的字符串
    - # json.dumps()能正常显示中文，需加入参数ensure_ascii=False
    """
    Dir, file = os.path.split(FilePath)
    _, suffix = os.path.splitext(file)
    # 先保证 有文件后缀，且后缀为 .json
    if suffix and suffix != ".json":
        raise TypeError("文件不是json文件类型，请输入正确的以 .json 为后缀的文件！")
    # 再保证目录存在，不存则就创建
    if Dir and not os.path.exists(Dir):  # 路径中的目录不为空，且不存在 的情况
        try:
            os.makedirs(Dir)  # 创建目录
        except OSError:
            raise TypeError("你输入的目录不正确！请输入文件的绝对路径，或者相对路径！相对路径是类似./dir/file的格式！")
    # 最后创建文件
    # 检查字符串是不是 字典 或 列表 格式的，确定并转成python对象（字典 或 列表 ）后，再保存到json文件
    if isinstance(Object, str):
        if not Object:
            with open(FilePath, "w", encoding="utf-8") as file:
                json.dump("", file, ensure_ascii=ensure_ascii)
        elif Object:
            try:
                if isinstance(eval(Object), (dict, list)):
                    Object = json.dumps(eval(Object))   # 1.用 eval方法 字典或列表格式的字符串转成 python对象，2.用 jumps方法 把python对象转成 json字符串格式
                    Object = json.loads(Object)  # 3.用 loads 方法把 字符串转成 字典或列表格式的字符串 转成 python对象
                    with open(FilePath, "w", encoding="utf-8") as file:
                        json.dump(Object, file, ensure_ascii=ensure_ascii)
                else:
                    raise TypeError("请输入，字典或列表 格式类型的字符串！")
            except NameError:
                raise TypeError("请输入，字典或列表 格式类型的字符串！")
    # 把 python对象（字典 或 列表 ）保存到json文件
    elif isinstance(Object, (dict, list)):
        with open(FilePath, "w", encoding="utf-8") as file:
            json.dump(Object, file, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    a = {1121: '3'}
    b = ['2', 2]
    c = "{'a': '小米', 'b': '小于'}"
    d = "file"
    to_json("ttt.json", a)
