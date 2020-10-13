"""
    生成测试报告
"""

# 1.生成 suite 对象
import unittest
import time

from case.TestITheimaLogin import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

# 2.执行suite对象将数据写入文件流
filename = "./report/" + time.strftime("%Y%m%d %H%M%S") + ".html"
with open(filename,"wb") as f:
    runner = HTMLTestRunner(f,title="测试报告",description="黑马头条接口测试")
    runner.run(suite)