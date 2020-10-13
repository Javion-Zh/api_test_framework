from pathlib import Path

# 封装 URL 前缀
import time

BASE_URL = "http://127.0.0.1/app/v1_0/"
# 获取项目的绝对路径
BASE_PATH = Path(__file__).resolve().parent
# 声明一个变量
TOKEN = None
