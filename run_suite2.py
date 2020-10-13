"""
    测试收藏接口:
        先登录，再收藏，需要使用 suite 对象组织执行逻辑

    组织执行逻辑后，仍然收藏失败，原因?
        因为，登录成功后，给客户端响应了一个称之为 token 的身份标记(类似于 cookie 、 银行卡)
        收藏操作时，第二次访问服务器(去银行)，需要提交身份标记 token
    解决策略:
        1.核心: 获取
        2.核心: 提交

"""

import unittest
from case.TestCollections import TestCollections
from case.TestITheimaLogin import TestLogin

# 1.创建 suite 对象
suite = unittest.TestSuite()
# 2.suite 对象组织 TestLogin("test_login") + TestCollections("test_collection")
suite.addTest(TestLogin("test_login"))
suite.addTest(TestCollections("test_collection"))
# 3.运行测试套件 TextTestRunner()
runner = unittest.TextTestRunner()
runner.run(suite)
