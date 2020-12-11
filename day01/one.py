# 引入包
import requests
import json
# 单元测试框架
import unittest
import allure_commons

class Test(unittest.TestCase):
    # 类里面的函数，第一个参数为self
    def test(self):
        '''请求的用例'''
        # 设置请求地址
        url = 'http://api.tianapi.com/txapi/xhzd/index'
        data = {
            'key': '2328169cc2883a60816189e5492f02dd',
            'word': 'wo',
            'type': '1'
        }
        # 定制头
        headers = {
            "content-type": 'application/json'
        }
        # 发送请求
        res = requests.post(url=url, data=data)
        print(res.text)
        print(type(res.text))
        print(type(res.content))
        # 转换为字典
        respone=json.loads(res.text)
        msg=respone['msg']
        # 设置断言
        self.assertEqual(msg,"success")

if __name__ == '__main__':
    unittest.main()