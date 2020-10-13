"""
    架构简介
        api == 请求业务(requests相关实现)
        case == 参数化+断言业务(unittest相关实现)
        data == 测试数据(一般使用 JSON 文件)
        report + tools + runsuite.py 生成测试报告
        app.py 封装常量和被复用的数据
"""
import os

# 封装 URL 前缀
import time

BASE_URL = "http://127.0.0.1/app/v1_0/"
# 获取项目的绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# 声明一个变量
TOKEN = None
