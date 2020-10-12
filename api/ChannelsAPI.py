"""
    封装请求业务:
        函数:获取频道列表的请求
"""
import app


class Channels:
    def __init__(self):
        self.get_channels_url = app.BASE_URL + "channels"


    # 获取频道列表
    def get_channels(self,session):
        return session.get(self.get_channels_url)

