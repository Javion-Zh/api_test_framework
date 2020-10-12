"""
    测试文章的收藏与取消收藏接口
"""
import unittest

import requests

from api.CollectionsAPI import Collections


class TestCollections(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.coll = Collections()

    def tearDown(self):
        self.session.close()


    #测试函数
    def test_coolection(self):
        # 收藏业务
        # response = collections对象.collec()
        response = self.coll.collec(self.session,"1")
        # 断言业务
        print(response.json())
        self.assertIn("OK",response.json().get("message"))
