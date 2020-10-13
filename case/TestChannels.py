"""
    测试频道列表:
        核心: case 需要调用 api
"""
import unittest

import requests

from api.ChannelsAPI import Channels


class TestChannels(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.chan = Channels()

    def tearDown(self):
        self.session.close()

    # 测试获取频道列表
    def test_get_channels(self):
        # 请求业务
        # response = channles对象.get_channels()
        response = self.chan.get_channels(self.session)
        # 断言业务
        print(response.json())
        self.assertIn("OK", response.json().get("message"))
