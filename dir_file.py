# 2023/3/27 21:14 Mae
"""
1. 获取目录中的文件，（.开头的文件，目录 和 __开头的目录，文件，默认不显示，如需要请设置 hideFiles=False）
2. 获取目录中所有的文件名
"""
from typing import Union
import os


def joinDirFilenameSuffix(*args: Union[str, tuple]):
    """合并 目录，文件名，文件后缀"""
    all_path = []
    if isinstance(args, tuple) and isinstance(args[0], str):
        filepath = os.path.join(args[0], args[1], args[2])
        all_path.append(filepath)
    elif isinstance(args, tuple) and isinstance(args[0], tuple):
        for i in args:
            filepath = os.path.join(i[0], i[1], i[2])
            all_path.append(filepath)
    return all_path


def mergeDotAndSuffix(*args: Union[str, tuple]):
    """合并 给后缀加点"""
    all_path = []
    if isinstance(args, str):
        result = ".{}".format(args) if "." not in args else args
        all_path.append(result)
    elif isinstance(args, tuple):
        for i in args:
            result = ".{}".format(i) if "." not in i else i
            all_path.append(result)
    return all_path


def getAll(DirPath, hideFiles=True):
    """获取目录下所有的 文件夹名 和 文件"""
    if not os.path.isdir(DirPath):
        raise OSError("系统中没有找到这个目录！")
    # 查看目录下所有的目录和文件
    ls = os.listdir(dirPath)  # 包含文件夹名 和 文件名（含后缀）
    # 找到指定文件
    result_list = []
    if hideFiles:  # 默认 隐藏 "."开头的文件  和  "__"开头结尾的文件
        for i in ls:
            # 不是 "."开头的目录或文件  和 不是 "__"开头结尾的目录或文件
            if not i.startswith(".", 0, 1) and (not i.startswith("__", 0, 2) and not i.endswith("__", -2)):
                result_list.append(i)
    else:
        result_list = ls
    return result_list


def getDirname(DirPath, hideFiles=True):
    """获取目录下所有的文件夹名"""
    if not os.path.isdir(DirPath):
        raise OSError("系统中没有找到这个目录！")
    # 查看目录下所有的目录和文件
    ls = os.listdir(dirPath)  # 包含文件夹名 和 文件名（含后缀）
    # 找到指定文件
    result_list = []
    if hideFiles:  # 默认 隐藏 "."开头的文件  和 "__"开头结尾的文件
        for i in ls:
            _, sf = os.path.splitext(i)  # 如果是目录，那么  splitext 后，元组第2个是空值（即表示是文件夹，不是文件）
            # 不是 "."开头的文件  和 不是 "__"开头结尾的文件 和 sf文件后缀不存在 即表示是文件夹名（排除文件）
            if not i.startswith(".", 0, 1) and \
                    (not i.startswith("__", 0, 2) and not i.endswith("__", -2)) and not sf:
                result_list.append(i)
    else:
        for i in ls:
            _, sf = os.path.splitext(i)  # 如果是目录，那么  splitext 后，元组第2个是空值（即表示是文件夹，不是文件）
            if not sf:  # sf文件后缀不存在 即表示是文件夹名（排除文件）
                result_list.append(i)
    return result_list


def getFile(DirPath, suffix: Union[None, str, tuple], hideFiles=True):
    """
    获取目录下所有的文件，或者指定的文件类型的文件

    - DirPath：目录的路径
    - suffix：文件的类型，例如[txt, json, jpg, png, xlsm, doc, ...]
    - - suffix = None，表示获取目录中所有文件类型的文件。
    - - hideFiles=True，表示隐藏 "."开头的文件  和 不是 "__"开头结尾的文件 的文件；False，目录下指定文件全是显示，也不隐藏这些文件。
    """
    if not os.path.isdir(DirPath):
        raise OSError("系统中没有找到这个目录！")
    # 查看目录下所有的目录和文件
    ls = os.listdir(dirPath)  # 包含文件夹名 和 文件名（含后缀）
    # 找到指定文件
    result_list = []
    if suffix is None:
        if hideFiles:  # 默认 隐藏 "."开头的文件  和  "__"开头结尾的文件
            for i in ls:
                _, sf = os.path.splitext(i)  # 如果是目录，那么  splitext 后，元组第2个是空值（即表示是文件夹，不是文件）
                # 不是 "."开头的文件  和 不是 "__"开头结尾的文件 和 sf文件后缀存在 即表示是文件（排除目录）
                if not i.startswith(".", 0, 1) and \
                        (not i.startswith("__", 0, 2) and not i.endswith("__", -2)) and sf:
                    result_list.append(i)
        else:
            for i in ls:
                _, sf = os.path.splitext(i)  # 如果是目录，那么  splitext 后，元组第2个是空值（即表示是文件夹，不是文件）
                if sf:
                    result_list.append(i)
    elif isinstance(suffix, str):
        result_suffix = suffix if "." in suffix else "." + suffix
        if hideFiles:  # 默认 隐藏 "."开头的文件  和 "__"开头结尾的文件
            for i in ls:
                # 不是 "."开头的文件  和 不是 "__"开头结尾的文件 和 有指定后缀的 文件
                if not i.startswith(".", 0, 1) and \
                        (not i.startswith("__", 0, 2) and not i.endswith("__", -2)) and result_suffix in i:
                    result_list.append(i)
        else:
            for i in ls:
                _, sf = os.path.splitext(i)  # 如果是目录，那么  splitext 后，元组第2个是空值（即表示是文件夹，不是文件）
                if sf:
                    result_list.append(i)
    elif isinstance(suffix, tuple):
        result_sf_ls = mergeDotAndSuffix(*suffix)
        if hideFiles:  # 默认 隐藏 "."开头的文件  和  "__"开头结尾的文件
            for i in ls:
                for j in result_sf_ls:
                    if not i.startswith(".", 0, 1) and \
                            (not i.startswith("__", 0, 2) and not i.endswith("__", -2)) and j in i:
                        result_list.append(i)
        else:
            for i in ls:
                for j in result_sf_ls:
                    if j in i:
                        result_list.append(i)
    return result_list


def getFilename(DirPath, suffix: Union[None, str, tuple], no_duplicate=True, hideFiles=True):
    """
    获取目录下所有的文件名，或者指定类型的文件名（不含文件后缀），可指定要不要重复的文件名

    - DirPath：目录的路径
    - suffix：文件的类型，例如[txt, json, jpg, png, xlsm, doc, ...]
    - no_duplicate：获取的文件名，要不要重复的。默认Ture，不要重复的文件名（去重复）；打开即 no_duplicate=False，获取全部类型的文件名时，
      不同类型同名的文件名，都会会获取到，这样的情况就会出现重复的文件名。

    """
    all_file_list = getFile(DirPath, suffix) if hideFiles else getFile(DirPath, suffix, hideFiles=False)
    if all_file_list:
        filenames = []
        for i in all_file_list:
            filename, _ = os.path.splitext(i)
            if no_duplicate:
                if filename not in filenames:  # 去重复的文件名
                    filenames.append(filename)
            else:
                filenames.append(filename)
        return filenames


if __name__ == '__main__':
    dirPath = r"/Users/mae/.local/lib/python3.9/site-packages/ToolsPackage_mae"
    # dirPath = r"/Users/mae/.local/lib/python3.9/site-packages/ToolsPa_mae"
    # getFile(dirPath, suffix=(".py", "json", ".ipynb"), hideFiles=False)
    # print(getAll(dirPath, hideFiles=True))
    # print(getDirname(dirPath, hideFiles=False))
    print(getFilename(dirPath, suffix="dfa"))
