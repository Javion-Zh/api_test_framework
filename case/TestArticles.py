"""
    测试文章推送接口
     核心: case 调用 api
"""
import unittest

import requests

from api.ArticlesAPI import Articles


class TestArticles(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.art = Articles()

    def tearDown(self):
        self.session.close()

    # 测试函数
    def test_get_articles(self):
        # 请求业务
        # response = articles 对象.get_articles()
        response = self.art.get_articles(self.session,"26")
        # 断言业务
        print(response.json())
        self.assertIn("OK",response.json().get("message"))