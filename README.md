# 基于 Requests 库的接口自动化测试框架

架构简介
- api == 请求业务(requests相关实现)
- case == 参数化+断言业务(unittest相关实现)
- data == 测试数据(一般使用 JSON 文件)
- report + tools + runsuite.py 生成测试报告
- app.py 封装常量和被复用的数据
