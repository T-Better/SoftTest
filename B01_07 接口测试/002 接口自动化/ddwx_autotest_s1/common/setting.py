#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入 os 模块，用于与操作系统进行交互
import os

# 从 typing 模块导入 Text 类型，用于注解函数参数和返回值的类型
from typing import Text

# 定义函数 root_path，用于获取根路径
def root_path():
    """ 获取 根路径 """
    # 使用 os 模块获取当前脚本所在目录的上一级目录，并返回路径
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path

# 定义函数 ensure_path_sep，用于处理不同操作系统路径分隔符的兼容性
def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    # 如果路径中包含斜杠 ("/")，则将其替换为当前操作系统的路径分隔符
    if "/" in path:
        path = os.sep.join(path.split("/"))

    # 如果路径中包含反斜杠 ("\\")，则将其替换为当前操作系统的路径分隔符
    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    # 返回根路径和处理后的路径拼接而成的结果
    return root_path() + path

